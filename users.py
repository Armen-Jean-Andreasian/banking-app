from bank_account import UserBankAccounts
from timer import Date


class User:
    def __init__(self, user_id):
        self.bank_account = UserBankAccounts(user_id)

    def check(self, start_date, end_date):
        now = Date.current_time()
        return self
