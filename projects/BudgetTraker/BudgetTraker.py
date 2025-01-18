import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt

class BudgetTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")
        self.root.geometry("600x400")

        self.transactions = []  # List to store transactions
        self.categories = ["Salary", "Business", "Rent", "Groceries", "Entertainment", "Miscellaneous"]

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Frame for transaction entry
        frame_entry = tk.Frame(self.root)
        frame_entry.pack(pady=20)

        # Labels and Entry for income/expense details
        tk.Label(frame_entry, text="Amount:").grid(row=0, column=0, padx=10)
        self.entry_amount = tk.Entry(frame_entry)
        self.entry_amount.grid(row=0, column=1)

        tk.Label(frame_entry, text="Description:").grid(row=1, column=0, padx=10)
        self.entry_description = tk.Entry(frame_entry)
        self.entry_description.grid(row=1, column=1)

        tk.Label(frame_entry, text="Category:").grid(row=2, column=0, padx=10)
        self.category_menu = ttk.Combobox(frame_entry, values=self.categories)
        self.category_menu.grid(row=2, column=1)
        self.category_menu.current(0)

        # Income/Expense type
        self.type_var = tk.StringVar(value="Income")
        tk.Radiobutton(frame_entry, text="Income", variable=self.type_var, value="Income").grid(row=3, column=0)
        tk.Radiobutton(frame_entry, text="Expense", variable=self.type_var, value="Expense").grid(row=3, column=1)

        # Add button
        tk.Button(frame_entry, text="Add Transaction", command=self.add_transaction).grid(row=4, column=0, columnspan=2, pady=10)

        # Display section
        frame_display = tk.Frame(self.root)
        frame_display.pack(pady=10)

        # Labels for displaying summary
        self.label_total_income = tk.Label(frame_display, text="Total Income: $0", font=("Arial", 12))
        self.label_total_income.pack(pady=5)

        self.label_total_expenses = tk.Label(frame_display, text="Total Expenses: $0", font=("Arial", 12))
        self.label_total_expenses.pack(pady=5)

        self.label_balance = tk.Label(frame_display, text="Balance: $0", font=("Arial", 14, "bold"))
        self.label_balance.pack(pady=5)

        # Buttons for actions
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Show Pie Chart", command=self.show_pie_chart).grid(row=0, column=0, padx=10)
        tk.Button(frame_buttons, text="Show Bar Chart", command=self.show_bar_chart).grid(row=0, column=1, padx=10)
        tk.Button(frame_buttons, text="Export to CSV", command=self.export_to_csv).grid(row=0, column=2, padx=10)

    def add_transaction(self):
        # Get data from entry fields
        try:
            amount = float(self.entry_amount.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for amount.")
            return
        
        description = self.entry_description.get()
        category = self.category_menu.get()
        trans_type = self.type_var.get()

        # Store transaction as a dictionary
        transaction = {
            "Amount": amount,
            "Description": description,
            "Category": category,
            "Type": trans_type
        }
        self.transactions.append(transaction)

        # Clear entries
        self.entry_amount.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)

        # Update totals and display
        self.update_summary()

    def update_summary(self):
        # Calculate total income, total expenses, and balance
        total_income = sum(t['Amount'] for t in self.transactions if t['Type'] == 'Income')
        total_expenses = sum(t['Amount'] for t in self.transactions if t['Type'] == 'Expense')
        balance = total_income - total_expenses

        # Update labels
        self.label_total_income.config(text=f"Total Income: ${total_income:.2f}")
        self.label_total_expenses.config(text=f"Total Expenses: ${total_expenses:.2f}")
        self.label_balance.config(text=f"Balance: ${balance:.2f}")

    def show_pie_chart(self):
        # Categorize transactions into expenses by category
        expense_data = {category: 0 for category in self.categories}
        for transaction in self.transactions:
            if transaction["Type"] == "Expense":
                expense_data[transaction["Category"]] += transaction["Amount"]

        # Filter out categories with zero expenses
        expense_data = {k: v for k, v in expense_data.items() if v > 0}

        if expense_data:
            plt.pie(expense_data.values(), labels=expense_data.keys(), autopct="%1.1f%%")
            plt.title("Expenses by Category")
            plt.show()
        else:
            messagebox.showinfo("No Data", "No expense data available to display.")

    def show_bar_chart(self):
        # Categorize transactions into income and expenses
        income_data = {category: 0 for category in self.categories}
        expense_data = {category: 0 for category in self.categories}

        for transaction in self.transactions:
            if transaction["Type"] == "Income":
                income_data[transaction["Category"]] += transaction["Amount"]
            else:
                expense_data[transaction["Category"]] += transaction["Amount"]

        # Prepare data for bar chart
        categories = list(self.categories)
        income_values = [income_data[category] for category in categories]
        expense_values = [expense_data[category] for category in categories]

        x = range(len(categories))
        plt.bar(x, income_values, width=0.4, label="Income", align="center")
        plt.bar(x, expense_values, width=0.4, label="Expenses", align="edge")
        plt.xticks(x, categories, rotation=45)
        plt.ylabel("Amount")
        plt.legend()
        plt.title("Income and Expenses by Category")
        plt.tight_layout()
        plt.show()

    def export_to_csv(self):
        # Convert transactions to DataFrame
        df = pd.DataFrame(self.transactions)
        df.to_csv("budget_data.csv", index=False)
        messagebox.showinfo("Export Success", "Transactions exported to 'budget_data.csv'")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()
