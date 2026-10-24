GST_PERCENT = 18

names = []
prices = []
quantities = []
line_totals = []

print("Enter items (type done as the item name to finish)")
while True:
    item = input("Item name: ").strip().title()
    if item == "Done":
        break
    price = float(input("Price per unit: "))
    qty = int(input("Quantity: "))

    amount = price * qty
    if qty >= 10:
        item_rate = 10
    elif qty >= 5:
        item_rate = 5
    else:
        item_rate = 0
    amount = amount - amount * item_rate / 100

    names.append(item)
    prices.append(price)
    quantities.append(qty)
    line_totals.append(amount)

if len(names) == 0:
    print("No items entered.")
    raise SystemExit

subtotal = sum(line_totals)

rule_names = []
rule_rates = []

if subtotal > 5000:
    rule_names.append("Bill value discount")
    rule_rates.append(10)
elif subtotal > 2000:
    rule_names.append("Bill value discount")
    rule_rates.append(5)

member = input("Loyalty member? (y/n): ").strip().lower()
if member == "y":
    rule_names.append("Member discount")
    rule_rates.append(3)

coupon = input("Coupon code (press Enter to skip): ").strip().upper()
if coupon == "FEST5":
    rule_names.append("Coupon FEST5")
    rule_rates.append(5)
elif coupon != "":
    print("Invalid coupon code.")

line = "-" * 46
print("\n" + line)
print("RETAIL BILL".center(46))
print(line)
print(f"{'Item':<16}{'Qty':>5}{'Price':>10}{'Amount':>12}")
for i in range(len(names)):
    print(f"{names[i]:<16}{quantities[i]:>5}{prices[i]:>10.2f}{line_totals[i]:>12.2f}")
print(line)
print(f"{'Subtotal (after item discounts)':<34}{subtotal:>12.2f}")

current = subtotal
for i in range(len(rule_names)):
    cut = current * rule_rates[i] / 100
    current = current - cut
    label = f"{rule_names[i]} ({rule_rates[i]}%)"
    print(f"{label:<34}{-cut:>12.2f}")

gst = current * GST_PERCENT / 100
print(f"{'GST (' + str(GST_PERCENT) + '%)':<34}{gst:>12.2f}")
print(f"{'TOTAL (Rs.)':<34}{current + gst:>12.2f}")
print(line)
