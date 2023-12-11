class Bank:
    ACCOUNTS = {}
    # user

    @classmethod
    def add_user(cls, username):
        cls.ACCOUNTS[username] = 0
        return cls

    @classmethod
    def get_balance(cls, username):
        if username not in cls.ACCOUNTS:
            cls.add_user(username)
            return cls.ACCOUNTS[username]
        else:
            return cls.ACCOUNTS[username]

    @classmethod
    def update_balance(cls, username, new_amount):
        cls.ACCOUNTS[username] = new_amount
        return cls


class UserBankAccount:
    def __init__(self, username):
        self.username = username
        self.balance = Bank.get_balance(self.username)

    def check_funds(self, period_start_date, period_end_date):





class UserTransactions(UserBankAccount):
    def save_balance(self):
        Bank.update_balance(self.username, self.balance)
        return self

    def top_up(self, amount):
        self.balance += amount
        self.save_balance()
        return self

    def withdraw(self, amount):
        self.balance += amount
        self.save_balance()
        return self
