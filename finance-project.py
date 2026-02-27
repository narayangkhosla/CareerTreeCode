# display the menu
# 1. when we define the function + call it
import datetime
import os
from datetime import datetime

DATA_FILE = "transactions.txt"
BUDGET_FILE = "budget.txt"


# 2026-02-25 20:46:03|income|Salary|300.0
def load_transactions():
    transactions = []
    """Load all the transactions from the file"""
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split("|")
                if len(parts) == 4:
                    transaction = {
                        "date": parts[0],
                        "type": parts[1],
                        "category": parts[2],
                        "amount": float(parts[3]),
                    }
                    transactions.append(transaction)
    return transactions


def save_transactions(transaction_type, category, amount):
    # capture the date/time too
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(DATA_FILE, "a") as file:
        file.write(f"{date}| {transaction_type}| {category}| {amount}\n")

    print(f" {transaction_type.capitalize()} of £{amount:.2f} recorded successfully.")


def add_income():
    """Add a new income transaction"""
    print("\n ---- Add Income ----")
    category = input("Category (e.g., Salary, Freelance, Gift)")
    while True:
        try:
            amount = float(input("Enter an amount: £"))
            if amount < 0:
                print("Amount must be positive")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number")
    # saving the transaction with the correct category and amount

    save_transactions("income", category, amount)


def add_expense():
    """Add a new expense transaction"""
    print("\n ---- Add Expense ----")
    category = input("Category (e.g., Food, Transport, Entertainment)")
    while True:
        try:
            amount = float(input("Enter an amount: £"))
            if amount < 0:
                print("Amount must be positive")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number")
    # saving the transaction with the correct category and amount
    save_transactions("expense", category, amount)


def view_all_transactions():
    transactions = load_transactions()
    if not transactions:
        print("\n No Transactions found.")
        return

    print("\n" + "=" * 70)
    print(f"{"Date":<20} {"Type":<10} {"Category":<20} {'Amount':>10}")

    for transaction in transactions:
        amount_str = f"£{transaction['amount']:.2f}"
        print(
            f"{transaction['date']:<20} {transaction['type']:<10} {transaction['category']:<20} {amount_str:>10}"
        )

    print("=" * 70)


def view_by_category():
    pass


def set_budget():
    print("\n--- Set Monthly Budget ---")

    while True:
        try:
            budget = float(input("Enter monthly budget amount: "))
            if budget < 0:
                print("Budget cannot be negative. Try again")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number")

    with open(BUDGET_FILE, "w") as file:
        file.write(str(budget))

    print(f"Monthly Budget set to: £{budget:,.2f}")


def load_budget():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as file:
            try:
                return float(file.read().strip())
            except ValueError:
                return 0
    return 0


def calculate_summary():
    transactions = load_transactions()
    if not transactions:
        print("\n No Transactions found.")
        return

    total_income = 0
    total_expenses = 0

    for transaction in transactions:
        if transaction["type"].strip() == "income":  # first_name == 'narayan '
            total_income += transaction["amount"]  # assignment addition

        elif transaction["type"].strip() == "expense":
            total_expenses += transaction["amount"]  # assignment addition

    balance = total_income - total_expenses

    print("\n" + "=" * 50)
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Balance: {balance:.2f}")


def clear_all_data():
    confirm = input("Type 'DELETE' to confirm: ").strip()
    if confirm == "DELETE":
        if os.path.exists(BUDGET_FILE):
            os.remove(BUDGET_FILE)
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
        print("All the data has been cleared successfully.")
    else:
        print("Operation Cancelled")


def display_menu():
    """This will display the list of options."""
    print("=" * 50)
    print("Personal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expenses")
    print("3. View All transactions")
    print("4. View Summary")
    print("5. View by Category")
    print("6. Set Monthly Budget")
    print("7. Clear All Data")
    print("8. Exit")
    print("=" * 50)


def main():
    print("\n Welcome to Personal Finance Tracker")

    while True:
        display_menu()
        choice = input("\n Enter your choice (1-8): => ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_all_transactions()
        elif choice == "4":
            calculate_summary()
        elif choice == "5":
            view_by_category()
        elif choice == "6":
            set_budget()
        elif choice == "7":
            clear_all_data()
        elif choice == "8":
            print("Thank you for using our system.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8")


main()
