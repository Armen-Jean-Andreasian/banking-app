class Bank:
    def __init__(self):
        self.user_balances = dict()
        # {user_id : [{login:password}, balance] }


class UserRegistration(Bank):
    def __init__(self, user_id, login, password):
        super().__init__()
        self.password = password
        self.login = login
        self.user_id = user_id

    def register_user(self):
        if self.user_id not in self.user_balances:
            self.user_balances[self.user_id] = 0


class UserLogin(Bank):
    def __init__(self, user_id, login, password):
        super().__init__()
        self.password = password
        self.login = login
        self.user_id = user_id

    def log_in(self):
        if self.user_id in self.user_balances:
            if {self.login: self.password} == self.user_balances[self.user_id][0]:
                pass
            else:
                raise ValueError("Incorrect username")
        else:
            raise ValueError("User not found")


class UserAccountMain(Bank):
    pass


class UserAccount(UserAccountMain):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    @property
    def get_balance(self):
        return self.user_balances[self.user_id]


class UserBankingApp(UserAccount):
    def __init__(self, user_id):
        super().__init__(user_id)
        try:
            self.user_balances[user_id]
        except KeyError:
            self.register_user()
        finally:
            self.current_balance = self.user_balances[user_id]

    def send_money(self, another_user_obj, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            another_user_obj.current_balance += amount
            return self
        else:
            raise "Insufficient funds"

    def top_up(self, amount):
        self.current_balance += amount
        return self


user_one = UserBankingApp(12)
user_one_balance = user_one.current_balance
print(user_one_balance)

user_one.top_up(5000)
print(user_one.current_balance)

user_two = UserBankingApp(34)
user_two_balance = user_two.current_balance
print(user_two_balance)

user_one.send_money(user_two, 1000)
print(user_one.current_balance)
print(user_two.current_balance)
