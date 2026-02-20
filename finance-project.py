# display the menu

def add_income():
    """Add a new income transaction"""
    print("\n ---- Add Income ----")
    category = input ('Category (e.g., Salary, Freelance, Gift)')
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



def add_expense():
    pass

def view_all_transactions():
    pass

def calculate_summary():
    pass
        
def view_by_category():
    pass
        
def set_budget():
    pass

def clear_all_data():
    pass

def display_menu():
    """This will display the list of options."""
    print("="*50)
    print("Personal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expenses")
    print("3. View All transactions")
    print("4. View Summary")
    print("5. View by Category")
    print("6. Set Monthly Budget")
    print("7. Clear All Data")
    print("8. Exit")
    print("="*50)

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
        elif choice == '8':
            print("Thank you for using our system.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8")

main()