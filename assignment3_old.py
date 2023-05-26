class BankAccount:
    def __init__(self, name, account_number, account_type, balance):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def validate_account_number(self):
        if len(self.account_number) != 10:
            print("Invalid account number. Account number must be 10 digits long.")
            return False
        return True

    def deposit(self, amount):
        if amount < 10000:
            print("Amount to be deposited must be more than 10000.")
            return

        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
            return

        self.balance -= amount
        print("Amount withdrawn successfully.")

    def display_details(self):
        print("Account Details:")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)


def create_bank_account():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number (10 digits): ")
    account_type = input("Enter account type: ")
    balance = float(input("Enter initial balance: "))

    account = BankAccount(name, account_number, account_type, balance)
    return account


# Main program
account = None

while True:
    print("\n----- Bank Account Menu -----")
    print("1. Create a new Bank Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Display Account Details")
    print("0. Exit")

    choice = input("Enter your choice (0-4): ")

    if choice == "1":
        account = create_bank_account()
        print("Bank account created successfully.")
    elif choice == "2":
        if account is None:
            print("No bank account found. Please create a new account first.")
        else:
            amount = float(input("Enter the amount to deposit: "))
            if account.validate_account_number():
                account.deposit(amount)
    elif choice == "3":
        if account is None:
            print("No bank account found. Please create a new account first.")
        else:
            amount = float(input("Enter the amount to withdraw: "))
            if account.validate_account_number():
                account.withdraw(amount)
    elif choice == "4":
        if account is None:
            print("No bank account found. Please create a new account first.")
        else:
            account.display_details()
    elif choice == "0":
        print("Thank you for using the Bank Account System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
