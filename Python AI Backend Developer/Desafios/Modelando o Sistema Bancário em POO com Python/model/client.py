from model.natural_person import Natural_Person

class Client(Natural_Person):
    def __init__(self, name, cpf, date_of_birth, address):
        super().__init__(name, cpf, date_of_birth)
        self.address = address
        self.accounts = []

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        try:
            self.accounts.append(account)
        except Exception as error:
            return error
        return True
