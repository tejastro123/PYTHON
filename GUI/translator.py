from tkinter import *
from tkinter import ttk, messagebox
import asyncio
from googletrans import LANGUAGES, Translator

# Initialize the main application window
root = Tk()
root.title("Google Translate")
root.geometry("1080x400")
root.configure(bg="white")

translator = Translator()  # Create a translator instance


def label_change():
    """Updates the labels dynamically based on combobox selections."""
    label1.config(text=combo1.get())
    label2.config(text=combo2.get())
    root.after(1000, label_change)


import asyncio
from googletrans import Translator


def translate_now():
    """Performs text translation using asynchronous calls."""
    try:
        text_ = text1.get(1.0, END).strip()  # Get input text
        from_lang = combo1.get()  # Source language
        to_lang = combo2.get()  # Target language

        if not text_:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        if to_lang == "SELECT LANGUAGE":
            messagebox.showwarning("Language Error", "Please select a target language.")
            return

        # Run the asynchronous translation
        loop = asyncio.get_event_loop()
        translated_text = loop.run_until_complete(async_translate(text_, from_lang, to_lang))

        text2.delete(1.0, END)
        text2.insert(END, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")


async def async_translate(text, from_lang, to_lang):
    """Asynchronous translation function."""
    translator = Translator()

    # Get language codes
    from_lang_code = next((code for code, lang in language.items() if lang.lower() == from_lang.lower()), None)
    to_lang_code = next((code for code, lang in language.items() if lang.lower() == to_lang.lower()), None)

    if not from_lang_code or not to_lang_code:
        raise ValueError("Selected languages are not supported.")

    # Translate text asynchronously
    result = await translator.translate(text, src=from_lang_code, dest=to_lang_code)
    return result.text


# Language data
language = LANGUAGES
languageV = list(language.values())

# Source language combobox
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 15", state="readonly")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

frame1 = Frame(root, bg="black", bd=5)
frame1.place(x=10, y=118, width=440, height=210)

text1 = Text(frame1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(frame1, command=text1.yview)
scrollbar1.pack(side="right", fill="y")
text1.configure(yscrollcommand=scrollbar1.set)

# Target language combobox
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 15", state="readonly")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="SELECT LANGUAGE", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

frame2 = Frame(root, bg="black", bd=5)
frame2.place(x=620, y=118, width=440, height=210)

text2 = Text(frame2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(frame2, command=text2.yview)
scrollbar2.pack(side="right", fill="y")
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate_button = Button(
    root,
    text="TRANSLATE",
    font="Roboto 15 bold italic",
    activebackground="purple",
    cursor="hand2",
    bd=5,
    bg="red",
    fg="white",
    command=translate_now
)
translate_button.place(x=465, y=250)

# Start dynamic label update
label_change()

# Run the application
root.mainloop()
