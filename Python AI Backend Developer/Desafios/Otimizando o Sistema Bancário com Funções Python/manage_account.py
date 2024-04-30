from datetime import datetime
from model.account import Account
from model.client import Client

class Manage_Account:

    def __init__(self):
        self.clients = []
        self.accounts = []
        self.operacoes = []

    def account_register(self, agency, _client):
        if _client:
            for client in self.clients:
                if client.cpf == _client.cpf:
                    nro = len(self.accounts) * 2 + 100
                    account = Account(agency, client, nro)
                    self.accounts.append(account)
                    print('Conta criada com sucesso')
                    print('numero - ', account.nro)
                    break
        else:
            print('Cliente nao cadastrado')

    def get_account(self, nro):
        if self.accounts:
            for account in self.accounts:
                if account.nro == nro:
                    return account
            print('Conta nao cadastrada')
        else:
            print('Nao ha contas cadastradas')

    def client_register(self, nome, cpf):
        if not self.clients:
            self.clients.append(Client(nome, cpf))
            print('Cliente cadastrado')
        else:
            for client in self.clients:
                if client.cpf == cpf:
                    print('Cpf ja cadastrado')
                    break

    def get_client(self, cpf):
        if self.clients:
            for client in self.clients:
                if client.cpf == cpf:
                    return client
            print('Cliente nao cadastrado')
        else:
            print('Nao ha clientes cadastrados')

    def list_account(self):
        if self.accounts:
            for account in self.accounts:
                print(account.client.nome, account.nro, account.saldo)
        else:
            print('Nao ha contas cadastradas')

    def deposito(self, valor, account, /):
        account.saldo += round(valor,2)
        self.operacoes.append(account.client.nome+' - '+str(+account.nro)+' - '+datetime.now().strftime('%d-%m-%Y - %H:%M')+' - deposito - '+str(valor))

    def saque(self, valor, account, /):
        account.saldo -= round(valor,2)
        account.LIMITE_SAQUE -= round(valor,2)
        account.LIMITE_DIARIO += 1
        self.operacoes.append(account.client.nome+' - '+str(+account.nro)+' - '+datetime.now().strftime('%d-%m-%Y - %H:%M')+' - saque - '+str(valor))

    def extrato(self, account):

        if len(self.operacoes) == 0:
            print('Nao foram realizadas movimentacoes')
        else:
            nro = str(account.nro)
            for operacao in self.operacoes:
                if nro in operacao:
                    print(operacao)
            print('Saldo - ' + str(round(account.saldo, 2)))

    def exeder_limite(self, valor, /, *, account):
        if account.saldo < valor:
            return True
        elif account.LIMITE_DIARIO > 3:
            return True
        elif valor > account.LIMITE_SAQUE:
            return True
        else:
            return False