while True:
    balance = float(input("Starting balance: "))
    if balance >= 0:
        break
    print("Starting balance cannot be negative.")

while True:
    deposit = float(input("Monthly deposit: "))
    if deposit > 0:
        break
    print("Monthly deposit must be positive.")

while True:
    rate = float(input("Monthly interest rate (%): "))
    if rate >= 0:
        break
    print("Interest rate cannot be negative.")

while True:
    goal = float(input("Savings goal: "))
    if goal > 0:
        break
    print("Savings goal must be positive.")

if balance >= goal:
    print("\nGoal already reached!")
    print(f"Final balance: {balance:.2f}")
else:
    month = 0
    total_interest = 0

    print("\nMonth | Interest | Balance")
    print("--------------------------")

    while month < 60:
        month += 1

        interest = balance * rate / 100
        balance += interest
        balance += deposit
        total_interest += interest

        print(f"{month:5} | {interest:8.2f} | {balance:7.2f}")

        if balance >= goal:
            break

    if balance >= goal:
        print(f"\nGoal reached in {month} months.")
    else:
        print("\nGoal not reached after 60 months.")

    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")