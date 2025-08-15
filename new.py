def calculate_monthly_budget(income, expenses):
    total_expenses = sum(expenses)
    savings = income - total_expenses

    budget = {
        "Income": income,
        "Total expenses": total_expenses,
        "Savings": savings
    }
    return budget

print('Welcome to the Monthly Budget Calculator')


income = float(input("Enter your monthly income: "))


num_expenses = int(input("Enter the number of expense categories: "))

expenses = []
for i in range(num_expenses):
    amount = float(input(f"Enter the amount for expense #{i+1}: "))
    expenses.append(amount)


budget = calculate_monthly_budget(income, expenses)

print("\n=== Monthly Budget Breakdown ===")
for category, amount in budget.items():
    print(f"{category}: GH₵{amount:.2f}")
def calculate_monthly_budget(income, expenses, savings_goal):
    total_expenses = sum(expenses)
    savings = income - total_expenses
    
    
    goal_met = savings >= savings_goal
    
    budget = {
        "Income": income,
        "Total expenses": total_expenses,
        "Savings": savings,
        "Goal Met": goal_met
    }
    return budget

print('Welcome to the Monthly Budget Calculator')


income = float(input("Enter your monthly income: "))


savings_goal = float(input("Enter your monthly savings goal: "))


num_expenses = int(input("Enter the number of expense categories: "))
expenses = []
expense_names = []

for i in range(num_expenses):
    name = input(f"Enter the name for expense #{i+1}: ")
    amount = float(input(f"Enter the amount for {name}: "))
    expenses.append(amount)
    expense_names.append(name)


budget = calculate_monthly_budget(income, expenses, savings_goal)

print("\n=== Monthly Budget Breakdown ===")
for category, amount in budget.items():
    if category != "Goal Met":
        print(f"{category}: GH₵{amount:.2f}")
    else:
        print(f"Savings Goal Met?: {'Yes' if amount else 'No'}")


if budget["Total expenses"] > budget["Income"]:
    print("\n⚠ Warning: Your expenses exceed your income!")


print("\n=== Expense Percentages ===")
for name, amount in zip(expense_names, expenses):
    percentage = (amount / income) * 100
    print(f"{name}: {percentage:.1f}% of income")
