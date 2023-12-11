class UserBankAccounts:
    balances = dict()

    def __init__(self, user_id):
        self.current_user_balance = 0
        self.user_id = user_id

        if self.user_id not in self.balances:
            self.balances[self.user_id] = 0
        else:
            self.current_user_balance = self.balances[self.user_id]

    def __update_records(self):
        self.balances[self.user_id] = self.current_user_balance
        return self

    def top_up(self, amount):
        self.current_user_balance += amount
        self.__update_records()

    def withdraw(self, amount):
        self.current_user_balance += amount
        self.__update_records()