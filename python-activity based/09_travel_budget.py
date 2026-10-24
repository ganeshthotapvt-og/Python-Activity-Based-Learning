currency_codes = ["USD", "EUR", "GBP", "AED", "SGD"]
rates_to_inr = [83.0, 90.0, 105.0, 22.6, 61.0]
categories = ["Flights", "Hotel", "Food", "Local transport", "Shopping"]
per_day = [False, True, True, True, False]

print("Supported currencies:", ", ".join(currency_codes), "(sample rates)")
code = input("Destination currency: ").strip().upper()
while code not in currency_codes:
    code = input("Not supported. Enter again: ").strip().upper()
rate = rates_to_inr[currency_codes.index(code)]

days = int(input("Number of days: "))
budget = float(input("Total budget in INR: "))

amounts_inr = []
print(f"\nEnter costs in {code} (hotel, food and transport are per day)")
for i in range(len(categories)):
    value = float(input(f"{categories[i]}: "))
    if per_day[i]:
        value = value * days
    amounts_inr.append(value * rate)

total = sum(amounts_inr)

line = "-" * 44
print("\n" + line)
print(f"TRAVEL BUDGET: {days} days, 1 {code} = Rs. {rate}")
print(line)
print(f"{'Category':<18}{'Amount (Rs.)':>14}{'Share':>10}")
top = 0
for i in range(len(categories)):
    share = amounts_inr[i] / total * 100
    print(f"{categories[i]:<18}{amounts_inr[i]:>14.2f}{share:>9.1f}%")
    if amounts_inr[i] > amounts_inr[top]:
        top = i
print(line)
print(f"{'Total':<18}{total:>14.2f}")
print(f"{'Budget':<18}{budget:>14.2f}")

if total <= budget:
    print(f"Status: Within budget, Rs. {budget - total:.2f} left")
else:
    print(f"Status: Over budget by Rs. {total - budget:.2f}")
print(f"Cost per day: Rs. {total / days:.2f}")
print("Highest spending on:", categories[top])
