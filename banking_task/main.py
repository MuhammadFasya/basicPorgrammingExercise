# main.py

from banking_system import Account

def main():
    account = None
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account = Account()
            print("Account created successfully!")
        elif choice == '2':
            if account:
                amount = input("Enter amount to deposit: ")
                try:
                    amount = float(amount)
                    if amount <= 0:
                        raise ValueError("Deposit amount must be positive.")
                    if account.deposit(amount):
                        print(f"${amount} deposited successfully!")
                    else:
                        print("Invalid deposit amount.")
                except ValueError as e:
                    print(e)
            else:
                print("Please create an account first.")
        elif choice == '3':
            if account:
                amount = input("Enter amount to withdraw: ")
                try:
                    amount = float(amount)
                    if amount <= 0:
                        raise ValueError("Withdraw amount must be positive.")
                    if account.withdraw(amount):
                        print(f"${amount} withdrawn successfully!")
                    else:
                        print("Invalid withdraw amount or insufficient balance.")
                except ValueError as e:
                    print(e)
            else:
                print("Please create an account first.")
        elif choice == '4':
            if account:
                balance = account.check_balance()
                print(f"Your current balance is: ${balance}")
            else:
                print("Please create an account first.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
