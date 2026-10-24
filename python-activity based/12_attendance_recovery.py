REQUIRED = 75

count = int(input("Number of subjects: "))
remaining = int(input("Classes remaining in the semester (per subject): "))

for i in range(count):
    subject = input(f"\nSubject {i + 1} name: ").strip().title()
    held = int(input("Classes held so far: "))
    attended = int(input("Classes attended: "))
    while attended > held or held == 0:
        print("Attended cannot be more than held, and held must be above 0.")
        held = int(input("Classes held so far: "))
        attended = int(input("Classes attended: "))

    percent = attended * 100 / held
    print(f"{subject}: {attended}/{held} = {percent:.1f}%")

    if percent >= REQUIRED:
        can_skip = 0
        while can_skip < remaining and (attended + remaining - can_skip - 1) * 100 / (held + remaining) >= REQUIRED:
            can_skip += 1
        print("Status: Safe")
        print(f"You can miss up to {can_skip} of the remaining {remaining} classes.")
    else:
        need = 0
        a = attended
        h = held
        while a * 100 / h < REQUIRED:
            a += 1
            h += 1
            need += 1
        print("Status: Shortage")
        if need <= remaining:
            print(f"Attend the next {need} classes continuously to reach {REQUIRED}%.")
        else:
            best = (attended + remaining) * 100 / (held + remaining)
            print(f"Cannot reach {REQUIRED}% even with full attendance. Maximum possible: {best:.1f}%")
            print("Apply for condonation or medical leave.")
