import pandas as pd
import openpyxl
import os

class BankAccount:
    def __init__(self, name, account_no, account_type, balance):
        self.name = name
        self.account_no = account_no
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Updated balance:", self.balance)
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Updated balance:", self.balance)
        else:
            print("Insufficient balance!")
    
    def display_info(self):
        print("Name:", self.name)
        print("Account number:", self.account_no)
        print("Account type:", self.account_type)
        print("Balance:", self.balance)
        
# Function to write data to an Excel file
def save_data(accounts):
    data = {"Name": [], "Account Number": [], "Account Type": [], "Balance": []}
    for account in accounts:
        data["Name"].append(account.name)
        data["Account Number"].append(account.account_no)
        data["Account Type"].append(account.account_type)
        data["Balance"].append(account.balance)
    df = pd.DataFrame(data)
    df.to_excel("ass3.xlsx", index=False)
    print("Data saved to ass3.xlsx")

# Function to read data from an Excel file
def load_data():
    try:
        df = pd.read_excel("ass3.xlsx")
        accounts = []
        for i, row in df.iterrows():
            account = BankAccount(row["Name"], row["Account Number"], row["Account Type"], row["Balance"])
            accounts.append(account)
        print("Data loaded from ass3.xlsx")
        return accounts
    except FileNotFoundError:
        print("File not found! Creating a new one.")
        return []

# Function to display the menu and get user input
def display_menu():
    print("\nMenu:")
    print("1. Add account")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("4. Display account info")
    print("5. Save data to file")
    print("6. Load data from file")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Main program
accounts = load_data()

while True:
    choice = display_menu()
    
    if choice == 1:
        name = input("Enter name: ")
        account_no = input("Enter account number: ")
        account_type = input("Enter account type: ")
        balance = float(input("Enter balance: "))
        account = BankAccount(name, account_no, account_type, balance)
        accounts.append(account)
        print("Account created successfully!")
        
    elif choice == 2:
        account_no = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        for account in accounts:
            if account.account_no == account_no:
                account.deposit(amount)
                break
        else:
            print("Account not found!")
            
    elif choice == 3:
        account_no = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        for account in accounts:
            if account.account_no == account_no:
                account.withdraw(amount)
                break
        else:
            print("Account not found!")
    
    elif choice == 4:
        account_no = input("Enter account number: ")
        for account in accounts:
            if account.account_no == account_no:
                print("Name:", account.name)
                print("Account number:", account.account_no)
                print("Account type:", account.account_type)
                print("Balance:", account.balance)
                break
        else:
            print("Account not found!")
    
    elif choice == 5:
        wb = openpyxl.load_workbook("ass3.xlsx")
        ws = wb.active
        for account in accounts:
            ws.append([account.name, account.account_no, account.account_type, account.balance])
        wb.save("ass3.xlsx")
        print("Data saved to ass3.xlsx file!")
        
    elif choice == 6:
        break
        
    else:
        print("Invalid choice! Please try again.") 
