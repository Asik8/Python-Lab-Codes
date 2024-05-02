# Define a class called BankAccount with attributes like account_holder_name, balance, and account_type (e.g., checking, savings). Implement methods to deposit, withdraw funds (with overdraft protection), and transfer money between accounts. Consider using inheritance to create different account types with specific interest rates or withdrawal limits.

# Tips:

# Remember to use self to refer to the current object within methods.
# Utilize docstrings to explain the purpose of your classes and methods.
# Test your code thoroughly to ensure it works as expected.


class BankAccount:
    def __init__(self, account_holder_name, balance=0.0, account_type='checking'):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}tk. Current balance: {self.balance}tk")
        else:
            print("Invalid amount to deposit.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}tk. Current balance: {self.balance}tk")
        else:
            print("Insufficient funds.")

    def transfer(self, destination_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            destination_account.balance += amount
            print(f"Transferred {amount}tk to {destination_account.account_holder_name}.")
            print(f"Your current balance: {self.balance}tk")
        else:
            print("Insufficient funds for transfer.")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name, balance=0.0, interest_rate=0.02):
        super().__init__(account_holder_name, balance, 'savings')
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}tk. Current balance: {self.balance}tk")


class CheckingAccount(BankAccount):
    def __init__(self, account_holder_name, balance=0.0, withdrawal_limit=500):
        super().__init__(account_holder_name, balance, 'checking')
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            super().withdraw(amount)
        else:
            print("Withdrawal amount exceeds limit.")


if __name__ == "__main__":
    account1 = BankAccount("M Asik", 1000.0)
    account2 = SavingsAccount("Motasem", 500.0, interest_rate=0.03)
    account3 = CheckingAccount("Billah", 2000.0, withdrawal_limit=1000)

    account1.deposit(200)
    account1.withdraw(100)
    account1.withdraw(1500)

    account1.transfer(account2, 300)
    account1.transfer(account2, 1000)

    account2.calculate_interest()
    account3.withdraw(800)