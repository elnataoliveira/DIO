from model.history import History
class Account:

    def __init__(self, number, client):
        self._sold = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, number, client):
        return cls(number, client)

    @property
    def sold(self):
        return self._sold

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history


    def withdraw(self, value):
        try:
            self._sold -= value
        except Exception as error:
            return error
        return True

    def deposit(self, value):
        try:
            self._sold += value
        except Exception as error:
            return error
        return True





