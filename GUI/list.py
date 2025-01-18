import tkinter as tk
from tkinter import messagebox

# Function to add task to the list
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task before adding")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to delete")

# Function to clear all tasks
def clear_all_tasks():
    listbox_tasks.delete(0, tk.END)

# Function to close the app
def exit_app():
    root.destroy()

# Create the root window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Add a frame for the task list
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=20)

# Create a listbox to display the tasks
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bd=2)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

# Add a scrollbar to the listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Entry box to add new tasks
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Buttons
button_add_task = tk.Button(root, text="Add Task", width=20, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", width=20, command=delete_task)
button_delete_task.pack(pady=5)

button_clear_tasks = tk.Button(root, text="Clear All Tasks", width=20, command=clear_all_tasks)
button_clear_tasks.pack(pady=5)

button_exit = tk.Button(root, text="Exit", width=20, command=exit_app)
button_exit.pack(pady=5)

# Run the GUI event loop
root.mainloop()
