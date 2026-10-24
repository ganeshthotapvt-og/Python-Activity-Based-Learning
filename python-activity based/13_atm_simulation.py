CORRECT_PIN = "1234"
DAILY_LIMIT = 20000
MIN_BALANCE = 500

balance = 15000
withdrawn_today = 0
statement = []

attempts = 0
logged_in = False
while attempts < 3:
    pin = input("Enter 4-digit PIN: ").strip()
    if pin == CORRECT_PIN:
        logged_in = True
        break
    attempts += 1
    print(f"Wrong PIN. {3 - attempts} attempt(s) left.")

if not logged_in:
    print("Card blocked. Please contact your bank.")
    raise SystemExit

print("\nWelcome to the ATM")
while True:
    print("\n1. Balance  2. Deposit  3. Withdraw  4. Mini statement  5. Exit")
    choice = input("Choose option: ").strip()

    if choice == "1":
        print(f"Available balance: Rs. {balance}")

    elif choice == "2":
        text = input("Deposit amount: ").strip()
        if text.isdigit() and int(text) > 0:
            amount = int(text)
            balance += amount
            statement.append(f"Deposit   +{amount:<7} Balance {balance}")
            print("Deposit successful.")
        else:
            print("Enter a valid amount.")

    elif choice == "3":
        text = input("Withdrawal amount: ").strip()
        if not text.isdigit() or int(text) <= 0:
            print("Enter a valid amount.")
        else:
            amount = int(text)
            if amount % 100 != 0:
                print("Amount must be a multiple of 100.")
            elif amount > balance - MIN_BALANCE:
                print(f"Insufficient balance. Rs. {MIN_BALANCE} must remain in the account.")
            elif withdrawn_today + amount > DAILY_LIMIT:
                print(f"Daily limit exceeded. You can still withdraw Rs. {DAILY_LIMIT - withdrawn_today} today.")
            else:
                balance -= amount
                withdrawn_today += amount
                statement.append(f"Withdraw  -{amount:<7} Balance {balance}")
                print("Please collect your cash.")

    elif choice == "4":
        if len(statement) == 0:
            print("No transactions yet.")
        else:
            print("Last transactions:")
            for entry in statement[-5:]:
                print(" ", entry)

    elif choice == "5":
        print("Thank you for banking with us.")
        break

    else:
        print("Invalid option.")
