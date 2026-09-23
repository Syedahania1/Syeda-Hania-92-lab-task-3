# Question No 4 - ATM Program

balance = 50000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: {balance}")

    elif choice == '2':
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"{amount} deposited successfully.")
            print(f"New balance is: {balance}")
        else:
            print("Invalid amount!")

    elif choice == '3':
        amount = int(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"New balance is: {balance}")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            print("Invalid amount!")

    elif choice == '4':
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
