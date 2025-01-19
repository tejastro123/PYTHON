from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

# Initialize the main application window
root = Tk()
root.title("Google Translate")
root.geometry("1080x400")
root.configure(bg="white")


def label_change():
    label1.config(text=combo1.get())
    label2.config(text=combo2.get())
    root.after(1000, label_change)


def translate_now():
    global language
    try:
        text_=text1.get(1.0,END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i,j in language.items():
                if(j == c3):
                    lan_ = i
            words = words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END, words)

    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")


# Load assets (update the paths to match your setup)
try:
    image_icon = PhotoImage(file="GUI/googletrans.png")
    root.iconphoto(False, image_icon)

    arrow_image = PhotoImage(file="GUI/arrow.png")
    image_label = Label(root, image=arrow_image, width=150, bg="white")
    image_label.place(x=460, y=50)
except Exception:
    messagebox.showwarning("Image Error", "Failed to load images. Check file paths.")


# Language data
language = googletrans.LANGUAGES
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
