slab_labels = ["First 100", "Next 100", "Next 100", "Above 300"]
slab_sizes = [100, 100, 100]
slab_rates = [3.50, 4.50, 6.00, 7.50]

FIXED_CHARGE = 50
DUTY_PERCENT = 5


def calculate_slabs(units):
    remaining = units
    used = []
    charges = []

    for i in range(len(slab_rates)):
        if i < len(slab_sizes):
            if remaining > slab_sizes[i]:
                take = slab_sizes[i]
            else:
                take = remaining
        else:
            take = remaining

        used.append(take)
        charges.append(take * slab_rates[i])
        remaining = remaining - take

    return used, charges


def usage_level(units):
    if units <= 100:
        return "Low usage"
    elif units <= 300:
        return "Moderate usage"
    else:
        return "High usage"


def print_bill(name, units):
    used, charges = calculate_slabs(units)

    energy_charge = sum(charges)
    duty = energy_charge * DUTY_PERCENT / 100
    total = energy_charge + FIXED_CHARGE + duty

    line = "-" * 44
    print("\n" + line)
    print("ELECTRICITY BILL".center(44))
    print(line)
    print("Customer :", name)
    print("Units    :", units, "(" + usage_level(units) + ")")
    print(line)
    print(f"{'Slab':<12}{'Units':>6}{'Rate':>8}{'Amount':>10}")

    for i in range(len(slab_labels)):
        if used[i] > 0:
            print(f"{slab_labels[i]:<12}{used[i]:>6}{slab_rates[i]:>8.2f}{charges[i]:>10.2f}")

    print(line)
    print(f"{'Energy charge':<26}{energy_charge:>18.2f}")
    print(f"{'Fixed charge':<26}{FIXED_CHARGE:>18.2f}")
    print(f"{'Duty (' + str(DUTY_PERCENT) + '%)':<26}{duty:>18.2f}")
    print(line)
    print(f"{'TOTAL (Rs.)':<26}{total:>18.2f}")
    print(line)

    return total


names = []
totals = []

while True:
    name = input("\nEnter customer name: ").strip().title()
    if name == "":
        print("Name cannot be empty.")
        continue

    units_text = input("Enter units consumed: ").strip()
    if not units_text.isdigit():
        print("Please enter units as a whole number.")
        continue

    units = int(units_text)
    total = print_bill(name, units)

    names.append(name)
    totals.append(total)

    again = input("\nGenerate another bill? (y/n): ").strip().lower()
    if again != "y":
        break

print("\nSUMMARY")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]:<15} Rs. {totals[i]:.2f}")
print("Total collection: Rs.", round(sum(totals), 2))
