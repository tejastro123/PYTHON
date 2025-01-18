
import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Load pre-trained model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Create the main chat class
class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chatbot")
        self.root.geometry("500x550")
        self.create_widgets()

    def create_widgets(self):
        # Chat history box
        self.chat_history = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled', width=60, height=20)
        self.chat_history.pack(padx=10, pady=10)

        # User input box
        self.entry_text = tk.Entry(self.root, width=50)
        self.entry_text.pack(padx=10, pady=10)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.handle_send)
        self.send_button.pack(pady=10)

    def handle_send(self):
        user_input = self.entry_text.get()
        if user_input.strip() != "":
            self.display_message(f"You: {user_input}", "user")
            self.get_bot_response(user_input)
            self.entry_text.delete(0, tk.END)

    def display_message(self, message, sender):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, message + '\n\n')
        self.chat_history.configure(state='disabled')
        self.chat_history.yview(tk.END)

    def get_bot_response(self, user_input):
        # Generate bot's response
        chat_input = chatbot(user_input)
        bot_response = chat_input[0]['generated_text']
        
        # Display bot's response
        self.display_message(f"Bot: {bot_response}", "bot")

# Run the chat application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
