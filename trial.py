def calculate_monthly_budget(income, expenses, savings_goal):
    total_expenses = sum(expenses)
    savings = income - total_expenses
    
    # Check if savings goal is met
    goal_met = savings >= savings_goal
    
    budget = {
        "Income": income,
        "Total expenses": total_expenses,
        "Savings": savings,
        "Goal Met": goal_met
    }
    return budget


print('Welcome to the Monthly Budget Calculator')

# Get income
income = float(input("Enter your monthly income: "))

# Get savings goal
savings_goal = float(input("Enter your monthly savings goal: "))

# Get expenses
num_expenses = int(input("Enter the number of expense categories: "))
expenses = []
expense_names = []

for i in range(num_expenses):
    name = input(f"Enter the name for expense #{i+1}: ")
    amount = float(input(f"Enter the amount for {name}: "))
    expenses.append(amount)
    expense_names.append(name)

# Calculate and display results
budget = calculate_monthly_budget(income, expenses, savings_goal)

print("\n=== Monthly Budget Breakdown ===")
for category, amount in budget.items():
    if category != "Goal Met":
        print(f"{category}: GH₵{amount:.2f}")
    else:
        print(f"Savings Goal Met?: {'Yes' if amount else 'No'}")

# Warning if expenses exceed income
if budget["Total expenses"] > budget["Income"]:
    print("\n⚠ Warning: Your expenses exceed your income!")

# Show percentage each expense takes from income
print("\n=== Expense Percentages ===")
for name, amount in zip(expense_names, expenses):
    percentage = (amount / income) * 100
    print(f"{name}: {percentage:.1f}% of income")

# Calculate total percentage spent and saved
total_percentage_spent = (budget["Total expenses"] / income) * 100
total_percentage_saved = (budget["Savings"] / income) * 100

print("\n=== Overall Percentages ===")
print(f"Total spent: {total_percentage_spent:.1f}% of income")
print(f"Total saved: {total_percentage_saved:.1f}% of income")
