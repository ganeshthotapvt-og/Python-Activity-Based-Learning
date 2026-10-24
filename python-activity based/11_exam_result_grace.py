subjects = ["Maths", "Physics", "Chemistry", "English", "Programming"]
PASS_MARK = 35
MAX_GRACE = 5

count = int(input("Number of students: "))
pass_count = 0
fail_count = 0

for s in range(count):
    name = input(f"\nStudent {s + 1} name: ").strip().title()
    marks = []
    for subject in subjects:
        text = input(f"{subject} marks (0-100): ").strip()
        while not text.isdigit() or int(text) > 100:
            text = input("Invalid. Enter marks between 0 and 100: ").strip()
        marks.append(int(text))

    failed = []
    for i in range(len(marks)):
        if marks[i] < PASS_MARK:
            failed.append(i)

    grace_used = 0
    if len(failed) == 0:
        result = "PASS"
    elif len(failed) == 1 and PASS_MARK - marks[failed[0]] <= MAX_GRACE:
        grace_used = PASS_MARK - marks[failed[0]]
        marks[failed[0]] = PASS_MARK
        result = "PASS (with grace)"
    else:
        result = "FAIL"

    total = sum(marks)
    percent = total / len(marks)

    if result == "FAIL":
        grade = "-"
    elif percent >= 75:
        grade = "Distinction"
    elif percent >= 60:
        grade = "First Class"
    elif percent >= 50:
        grade = "Second Class"
    else:
        grade = "Pass Class"

    print(f"--- {name} ---")
    for i in range(len(subjects)):
        note = ""
        if i in failed and result == "FAIL":
            note = "  (failed)"
        elif i in failed:
            note = f"  (+{grace_used} grace)"
        print(f"{subjects[i]:<14}{marks[i]:>4}{note}")
    print(f"Total {total}/500 | Percentage {percent:.1f}% | Result: {result} | Grade: {grade}")

    if result == "FAIL":
        fail_count += 1
    else:
        pass_count += 1

print("\nPassed:", pass_count, "| Failed:", fail_count)
print(f"Pass percentage: {pass_count / count * 100:.1f}%")
