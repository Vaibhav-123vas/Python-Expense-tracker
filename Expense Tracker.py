#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import matplotlib.pyplot as plt
from datetime import datetime


class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"Expense(amount={self.amount}, category={self.category}, description={self.description}, date={self.date})"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print("Expense added successfully.")

    def update_expense(self, index, amount=None, category=None, description=None):
        if 0 <= index < len(self.expenses):
            if amount is not None:
                self.expenses[index].amount = amount
            if category is not None:
                self.expenses[index].category = category
            if description is not None:
                self.expenses[index].description = description
            print("Expense updated successfully.")
        else:
            print("Invalid expense index.")

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self):
        expenses_by_category = {}
        for expense in self.expenses:
            if expense.category not in expenses_by_category:
                expenses_by_category[expense.category] = 0
            expenses_by_category[expense.category] += expense.amount
        return expenses_by_category

    def generate_summary_report(self):
        total_expenses = self.get_total_expenses()
        expenses_by_category = self.get_expenses_by_category()
        report = {
            "total_expenses": total_expenses,
            "expenses_by_category": expenses_by_category
        }
        return report

    def save_expenses(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump([expense.__dict__ for expense in self.expenses], f, indent=4)
            print("Expenses saved successfully.")
        except Exception as e:
            print(f"Error saving expenses: {e}")

    def load_expenses(self, filename):
        try:
            with open(filename, 'r') as f:
                expenses_data = json.load(f)
                self.expenses = [Expense(**expense) for expense in expenses_data]
            print("Expenses loaded successfully.")
        except Exception as e:
            print(f"Error loading expenses: {e}")

    def visualize_expenses_by_category(self):
        expenses_by_category = self.get_expenses_by_category()
        categories = list(expenses_by_category.keys())
        amounts = list(expenses_by_category.values())

        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Expenses by Category')
        plt.show()


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Remove Expense")
        print("4. Generate Summary Report")
        print("5. Save Expenses")
        print("6. Load Expenses")
        print("7. Visualize Expenses by Category")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            index = int(input("Enter expense index to update: "))
            amount = float(input("Enter new amount (or press Enter to skip): ") or "nan")
            category = input("Enter new category (or press Enter to skip): ")
            description = input("Enter new description (or press Enter to skip): ")
            tracker.update_expense(
                index, 
                None if amount != amount else amount, 
                None if not category else category, 
                None if not description else description
            )
        elif choice == '3':
            index = int(input("Enter expense index to remove: "))
            tracker.remove_expense(index)
        elif choice == '4':
            report = tracker.generate_summary_report()
            print("\nSummary Report")
            print(f"Total Expenses: {report['total_expenses']}")
            print("Expenses by Category:")
            for category, amount in report['expenses_by_category'].keys():
                print(f"{category}: {amount}")
        elif choice == '5':
            filename = input("Enter filename to save expenses: ")
            tracker.save_expenses(filename)
        elif choice == '6':
            filename = input("Enter filename to load expenses: ")
            tracker.load_expenses(filename)
        elif choice == '7':
            tracker.visualize_expenses_by_category()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# In[ ]:




