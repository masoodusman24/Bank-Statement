def show_balance(balance):
    print("******************")
    print(f"Your balance is ${balance:.2f}")
    print("******************")

def deposit():
    print("******************")
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid deposit amount. Must be greater than 0.")
            print("******************")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        print("******************")
        return 0

def withdraw(balance):
    print("******************")
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
            print("******************")
            return 0
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            print("******************")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        print("******************")
        return 0

def main():
    balance = 0.0
    is_running = True

    while is_running:
        print("******************")
        print("Banking Program")
        print("******************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("******************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("******************")
            print("That is not a valid choice. Please select 1, 2, 3, or 4.")
            print("******************")

    print("******************")
    print("Thank you! Have a nice day!")
    print("******************")

if __name__ == "__main__":
    main()
