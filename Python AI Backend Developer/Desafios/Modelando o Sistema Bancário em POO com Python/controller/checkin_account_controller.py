from model.checking_account import Checking_Account
from datetime import datetime

class Checking_Account_Controller:
    def __init__(self):
        self.accounts = []
        self.operacoes = []

    def account_register(self, _client, cliente_controller):

        clients = cliente_controller.list_clients
        print(clients[0].name)
        if clients:
            for client in clients:
                if client.cpf == _client.cpf:
                    number = len(self.accounts) * 2 + 100
                    account = Checking_Account(number, client)
                    self.accounts.append(account)
                    print('Conta criada com sucesso')
                    print('numero - ', account.number)
                    break
        else:
            print('Cliente nao cadastrado')

    def get_account(self, number):
        if self.accounts:
            for account in self.accounts:
                if account.number == number:
                    return account
            print('Conta nao cadastrada')
        else:
            print('Nao ha contas cadastradas')

    def list_account(self):
        if self.accounts:
            for account in self.accounts:
                print('NOME: ' + account.client.name, 'CC: ' + str(account.number), 'SALDO R$ - ' + str(account.sold)+' - '+str(account.daily_limit)+' - '+str(account.withdraw_limit))
        else:
            print('Nao ha contas cadastradas')

    def is_deposited(self, value, account, /):
        self.operacoes.append(
            'NOME: ' + account.client.name + ' CC:  ' + str(+account.number) + ' DATA ' + datetime.now().strftime(
                '%d-%m-%Y - %H:%M') + ' - deposito R$: ' + str(value))
        return account.deposit(value)

    def is_withdrew(self, value, account, /):
        self.operacoes.append(
            'NOME: ' + account.client.name + ' CC:  ' + str(+account.number) + ' DATA ' + datetime.now().strftime(
                '%d-%m-%Y - %H:%M') + ' - saque R$: ' + str(value))
        return account.withdraw(value)

    def bank_statment(self, account):

        if len(self.operacoes) == 0:
            print('Nao foram realizadas movimentacoes')
        else:
            number = str(account.number)
            for operacao in self.operacoes:
                if number in operacao:
                    print(operacao)
            print('Saldo - ' + str(round(account.saldo, 2)))

    def exceed_limit(self, value, /, *, account):
        if account.sold < value:
            return True
        elif account.daily_limit < 1:
            return True
        elif value > account.withdraw_limit:
            return True
        else:
            account.set_daily_limit()
            account.set_withdraw_limit(value)
            return False