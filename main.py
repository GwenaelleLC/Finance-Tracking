from Expenses import*
from User import*

def main():
    print("Welcome to the Financial Tracking App!")
    while True:
        print("\nMain Menu:")
        print("1. Create an account")
        print("2. Log in")
        print("3. Quit")
        choice = input("Please choose an option: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            if User.create_account(username, password):
                print("Account created successfully.")
            else:
                print("Error during account creation.")
        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            user = User.login(username, password)
            if user:
                print("Logged in successfully.")
                while True:
                    print("\nUser Menu:")
                    print("1. Add an expense")
                    print("2. View expense history")
                    print("3. Remove an expense")
                    print("4. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == '1':
                        amount = float(input("Amount of the expense: "))
                        category = input("Category of the expense (Food, Transport, Activity, Health): ")
                        user.add_expense(amount, category)
                        print("Expense added successfully.")
                    elif user_choice == '2':
                        expenses = user.get_expense_history()
                        if expenses:
                            print("Listing all your expenses:")
                            for index, expense in enumerate(expenses):
                                print(f"{index}: Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']}")
                        else:
                            print("No expenses recorded.")
                    elif user_choice == '3':
                        index = int(input("Enter the index of the expense to remove: "))
                        if user.remove_expense(index):
                            print("Expense removed successfully.")
                        else:
                            print("Failed to remove expense. Please check the index.")
                    elif user_choice == '4':
                        break
            else:
                print("Login failed. Please check your credentials.")
        elif choice == '3':
            print("Thank you for using the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()