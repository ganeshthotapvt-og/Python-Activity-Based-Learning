fee = float(input("Registration fee per participant: "))
participants = int(input("Expected participants: "))
registration_income = fee * participants

sponsor_names = []
sponsor_amounts = []
print("\nEnter sponsors (type done to finish)")
while True:
    sponsor = input("Sponsor name: ").strip().title()
    if sponsor == "Done":
        break
    sponsor_names.append(sponsor)
    sponsor_amounts.append(float(input("Amount: ")))

expense_names = []
expense_amounts = []
print("\nEnter expenses (type done to finish)")
while True:
    expense = input("Expense name: ").strip().title()
    if expense == "Done":
        break
    expense_names.append(expense)
    expense_amounts.append(float(input("Amount: ")))

sponsor_total = sum(sponsor_amounts)
total_income = registration_income + sponsor_total
total_expense = sum(expense_amounts)
surplus = total_income - total_expense

line = "-" * 44
print("\n" + line)
print("EVENT FINANCIAL PLAN".center(44))
print(line)
print(f"{'Registration fees':<30}{registration_income:>14.2f}")
for i in range(len(sponsor_names)):
    print(f"{'Sponsor: ' + sponsor_names[i]:<30}{sponsor_amounts[i]:>14.2f}")
print(f"{'Total income':<30}{total_income:>14.2f}")
print(line)
for i in range(len(expense_names)):
    share = expense_amounts[i] / total_expense * 100
    if share > 20:
        tag = "Major"
    else:
        tag = ""
    print(f"{expense_names[i]:<20}{expense_amounts[i]:>12.2f}{share:>8.1f}%  {tag}")
print(f"{'Total expenses':<30}{total_expense:>14.2f}")
print(line)

if surplus >= 0:
    print(f"Surplus : Rs. {surplus:.2f}")
else:
    print(f"Deficit : Rs. {-surplus:.2f}")

margin = surplus / total_expense * 100
if surplus < 0:
    status = "Deficit - reduce expenses or raise the fee"
elif margin < 10:
    status = "Risky - safety margin below 10%"
else:
    status = "Healthy"
print("Status  :", status)

needed = (total_expense - sponsor_total) / fee
break_even = int(needed)
if break_even < needed:
    break_even = break_even + 1
if needed <= 0:
    break_even = 0
print("Break-even participants:", break_even)
