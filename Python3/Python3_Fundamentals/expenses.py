# List of expenses

expenses = []
num_expenses = int(input("Enter your # of expenses:\n"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:\n")))

total = sum(expenses)

print(f"You spent ${total} this week.")