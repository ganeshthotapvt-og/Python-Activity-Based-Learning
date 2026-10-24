names = []
units = []
materials = []
labours = []
prices = []

count = int(input("Number of products: "))
overhead = float(input("Total fixed overhead for the month: "))

for i in range(count):
    names.append(input(f"\nProduct {i + 1} name: ").strip().title())
    units.append(int(input("Units produced and sold: ")))
    materials.append(float(input("Material cost per unit: ")))
    labours.append(float(input("Labour cost per unit: ")))
    prices.append(float(input("Selling price per unit: ")))

overhead_per_unit = overhead / sum(units)

print(f"\n{'Product':<12}{'Cost/unit':>10}{'Revenue':>11}{'Profit':>11}{'Margin%':>9}{'BEP units':>11}  Status")
profits = []
for i in range(count):
    cost_per_unit = materials[i] + labours[i] + overhead_per_unit
    revenue = prices[i] * units[i]
    profit = revenue - cost_per_unit * units[i]
    margin = profit / revenue * 100

    contribution = prices[i] - materials[i] - labours[i]
    if contribution > 0:
        bep = overhead_per_unit * units[i] / contribution
        bep_text = str(round(bep))
    else:
        bep_text = "N/A"

    if profit < 0:
        status = "Loss"
    elif margin < 10:
        status = "Low profit"
    elif margin < 25:
        status = "Good"
    else:
        status = "Excellent"

    profits.append(profit)
    print(f"{names[i]:<12}{cost_per_unit:>10.2f}{revenue:>11.2f}{profit:>11.2f}{margin:>9.1f}{bep_text:>11}  {status}")

best = 0
for i in range(count):
    if profits[i] > profits[best]:
        best = i

print("\nOverhead per unit    :", round(overhead_per_unit, 2))
print("Total profit         :", round(sum(profits), 2))
print("Most profitable item :", names[best])
