class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount} грн. Баланс: {self.balance} грн.")
        else:
            print("Сума повинна бути більше нуля")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount} грн. Баланс: {self.balance} грн.")
        else:
            print("Недостатньо коштів або неправильна сума")

    def get_balance(self):
        return self.balance


account = BankAccount("UA1234567890", 1000)
account.deposit(500)
account.withdraw(300) 
print(account.get_balance())
