print("CTI-110 P1HW2 - Travel Expense\n")
import datetime
today = datetime.datetime.now().date()
print("Date:", today)
print("Brigit Giles")

print("\nThis program calculates and display travel expenses\n")

budget = float(input("\nEnter budget:$ "))

destination = input("\nEnter your travel destination: ")

gas_expense = float(input("\nHow much do you think you will spend on gas:$ "))

accommodation_expense = float(input("\nApproximately, how much you need for accommodation/hotel:$ "))

food_expense = float(input("\nLast, how much do you need for food: $ "))

# Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("\n----------Travel Expenses----------")
print("Travel Location: ", destination)
print("Initial Budget: ", budget)
print("\nFuel: ",gas_expense)
print("Accomodation: ",accommodation_expense)
print("Food: ",food_expense) 
print("\nTotal Expenses: $%.2f " % total_expenses)
print("Remaining Budget: $%.2f " % remaining_budget)
