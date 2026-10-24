ward_names = ["General", "Semi-Private", "Private", "ICU"]
ward_rates = [1000, 2000, 3500, 7000]


def classify_patient(age):
    if age < 18:
        return "Pediatric", 5
    elif age < 60:
        return "Adult", 0
    else:
        return "Senior Citizen", 10


def stay_type(days):
    if days <= 2:
        return "Short stay"
    elif days <= 7:
        return "Regular stay"
    else:
        return "Long stay"


name = input("Patient name: ").strip().title()
age = int(input("Age: "))
days = int(input("Days admitted: "))

print("\nWard types")
for i in range(len(ward_names)):
    print(f"{i + 1}. {ward_names[i]:<14} Rs. {ward_rates[i]} per day")
choice = int(input("Choose ward number: "))
while choice < 1 or choice > len(ward_names):
    choice = int(input("Invalid choice. Choose ward number: "))

service_names = []
service_costs = []
print("\nEnter services (type done to finish)")
while True:
    service = input("Service name: ").strip().title()
    if service == "Done":
        break
    service_names.append(service)
    service_costs.append(float(input("Charge: ")))

ward = ward_names[choice - 1]
room_charge = days * ward_rates[choice - 1]
subtotal = room_charge + sum(service_costs)

category, discount_percent = classify_patient(age)
discount = subtotal * discount_percent / 100
total = subtotal - discount

line = "-" * 44
print("\n" + line)
print("HOSPITAL BILL".center(44))
print(line)
print("Patient  :", name)
print("Category :", category, "| Age", age)
print("Stay     :", stay_type(days), f"({days} days)")
print("Ward     :", ward)
if ward == "ICU":
    print("Note     : Critical care patient")
print(line)
print(f"{'Room charges':<30}{room_charge:>14.2f}")
for i in range(len(service_names)):
    print(f"{service_names[i]:<30}{service_costs[i]:>14.2f}")
print(line)
print(f"{'Subtotal':<30}{subtotal:>14.2f}")
print(f"{'Discount (' + str(discount_percent) + '%)':<30}{-discount:>14.2f}")
print(f"{'TOTAL (Rs.)':<30}{total:>14.2f}")
print(line)
