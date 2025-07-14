# A BUDGET MANAGER PROGRAM
# Start with a welcome message
# Ask for user's income (salary)
# Ask for user's income (business)
# Calculate total income
# Ask for user's to input transport expenses
# Ask for food expenses
# Calculate total income
# Calculate total expenses
# Summary

username = input("What is your name?: ")
print(f"Welcome {username} to Budget Manager!")

salary = float(input("What is your monthly income (salary)?:"))
business = float(input("What is your monthly business income?:"))

total_income = salary + business
print(f"Your total monthly income: Kshs.{total_income:.2f}")

transport = float(input("What is your Transport expenses for the month?:"))
food = float(input("What is your food expenses for the month?:"))
total_expenses = transport + food
print(f"Total expenses for the month: Kshs.{total_expenses:.2f}")

monthly_savings = total_income - total_expenses
print(f"Total monthly savings: Kshs.{monthly_savings:.2f}")

