balance = 10000

print("Bank Service")
print("Opening Balance:", balance)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Current Balance: Rs.", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful.")
            print("Updated Balance: Rs.", balance)
        else:
            print("Invalid amount")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Updated Balance: Rs.", balance)

        else:
            print("Insufficient balance.")
            print("Current Balance: Rs.", balance)

    elif choice == 4:
        print("Exitt")
        break

    else:
        print("Invalid choice")
