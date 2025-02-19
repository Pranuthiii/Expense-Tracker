class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, description):
        expense = {
            'category': category,
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
        else:
            print("\nExpense List:")
            for expense in self.expenses:
                print(f"\nCategory: {expense['category']}")
                print(f"Amount: ${expense['amount']}")
                print(f"Description: {expense['description']}")
                print("-" * 30)

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(category, amount, description)

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.total_expenses()

        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
