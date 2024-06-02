# Project1 - Develope a Personal Expense Tracker with graphical representation

import matplotlib.pyplot as plt

# Function to track income and expenses
def financial_tracker():
    expenses = {}
    total_expenses = 0
    income = int(input("Enter your income for the month: "))
    remaining_budget = income

    print("\nWelcome to the Personal Financial Tracker!")
    while True:
        print("\n 1.Add Expense\n 2.View Expenses\n 3.View Reamaining Budget\n 4.Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            item = input("Enter expense item: ")
            cost = int(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            total_expenses= total_expenses + cost
            remaining_budget=remaining_budget - cost
            if category in expenses:
                expenses[category] += cost
            else:
                expenses[category] = cost
            print("Expense added successfully!")

            # Check if expenses exceed a set limit
            expense_limit = 0.6 * income  # 60% of income
            if total_expenses > expense_limit:
                print("Alert: Your expenses have exceeded 60% of your income!")

        elif choice == '2':
            print("\nExpense Summary:")
            for category, cost in expenses.items():
                print(f"{category}: Rs.{cost:.2f}")

            print(f"\nTotal Expenses: Rs.{total_expenses:.2f}")
            # Plotting expenses
            plt.figure(figsize=(7, 5))
            plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.title('Expense Distribution')
            plt.show()

        elif choice == '3':
            print(f"\nRemaining Budget: Rs.{remaining_budget:.2f}")

        elif choice == '4':
            print("Thank you for using the Financial Tracker!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

financial_tracker()