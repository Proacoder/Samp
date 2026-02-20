class BankAccount:
    # Class Attributes
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self, account_holder, initial_deposit=0):
        self.account_holder = account_holder
        self.balance = initial_deposit

        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print("Deposit successful.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print("Withdrawal successful.")

    def display_account_info(self):
        print("\n--- Account Information ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

    @classmethod
    def display_bank_summary(cls):
        print("\n--- Bank Summary ---")
        print(f"Bank Name: {cls.bank_name}")
        print(f"Total Accounts: {cls.total_accounts}")
        print(f"Total Bank Balance: {cls.total_bank_balance}")


# -------------------------------
# User Interactive Menu
# -------------------------------

accounts = {}

while True:
    print("\n===== Bank Menu =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account Info")
    print("5. Display Bank Summary")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter account holder name: ")
        initial = float(input("Enter initial deposit: "))
        account = BankAccount(name, initial)
        accounts[name] = account
        print("Account created successfully.")

    elif choice == "2":
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[name].deposit(amount)
        else:
            print("Account not found.")

    elif choice == "3":
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = float(input("Enter withdrawal amount: "))
            accounts[name].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        name = input("Enter account holder name: ")
        if name in accounts:
            accounts[name].display_account_info()
        else:
            print("Account not found.")

    elif choice == "5":
        BankAccount.display_bank_summary()

    elif choice == "6":
        print("Thank you for using National Bank System.")
        break

    else:
        print("Invalid choice. Please try again.")