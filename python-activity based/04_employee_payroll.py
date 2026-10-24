names = []
gross_list = []
deduction_list = []
net_list = []

count = int(input("Number of employees: "))

for i in range(count):
    name = input(f"\nEmployee {i + 1} name: ").strip().title()
    basic = float(input("Basic salary: "))

    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da

    pf = basic * 0.12

    if gross > 20000:
        prof_tax = 200
    elif gross > 15000:
        prof_tax = 150
    else:
        prof_tax = 0

    if gross <= 25000:
        tax_rate = 0
    elif gross <= 50000:
        tax_rate = 5
    else:
        tax_rate = 10
    income_tax = gross * tax_rate / 100

    deductions = pf + prof_tax + income_tax
    net = gross - deductions

    print(f"--- Payslip: {name} ---")
    print(f"Basic {basic:.2f} + HRA {hra:.2f} + DA {da:.2f} = Gross {gross:.2f}")
    print(f"PF {pf:.2f} | Prof. tax {prof_tax:.2f} | Income tax {income_tax:.2f}")
    print(f"Total deductions {deductions:.2f} | Net salary {net:.2f}")

    names.append(name)
    gross_list.append(gross)
    deduction_list.append(deductions)
    net_list.append(net)

print("\nDEDUCTION ANALYSIS")
print(f"{'Name':<14}{'Gross':>10}{'Deduct':>10}{'Net':>10}{'Ded %':>8}  Level")
best = 0
for i in range(len(names)):
    percent = deduction_list[i] / gross_list[i] * 100
    if percent > 20:
        level = "High"
    elif percent > 10:
        level = "Medium"
    else:
        level = "Low"
    print(f"{names[i]:<14}{gross_list[i]:>10.2f}{deduction_list[i]:>10.2f}{net_list[i]:>10.2f}{percent:>8.1f}  {level}")
    if net_list[i] > net_list[best]:
        best = i

print("\nTotal gross pay      :", round(sum(gross_list), 2))
print("Total deductions     :", round(sum(deduction_list), 2))
print("Average net salary   :", round(sum(net_list) / len(net_list), 2))
print("Highest net salary   :", names[best], "-", round(net_list[best], 2))
