from model.account import Account


class Checking_Account(Account):
    def __init__(self, number, client, daily_limit=3, withdraw_limit=500):
        super().__init__(number, client)
        self._daily_limit = daily_limit
        self._withdraw_limit = withdraw_limit

    @property
    def daily_limit(self):
        return self._daily_limit

    @property
    def withdraw_limit(self):
        return self._withdraw_limit

    def set_daily_limit(self):
        self._daily_limit -= 1

    def set_withdraw_limit(self, value):
        self._withdraw_limit -= value

    def __str__(self):
        return f'''\
            Agency:\t{self.agency}
            C/C:\t\t{self.number}
            Titulary:\t{self.client.name}
        '''
