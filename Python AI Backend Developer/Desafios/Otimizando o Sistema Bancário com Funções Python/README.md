## Otimizando o Sistema Bancário com Funções Python

[função main](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Otimizando%20o%20Sistema%20Banc%C3%A1rio%20com%20Fun%C3%A7%C3%B5es%20Python/main.py)

```
import os
from model.manage_account import Manage_Account


def menu():
    return '''\n
================ MENU ================
    d - \tdepositar
    s - \tsacar
    e - \textrato
    c - \tcadastrar_client
    r - \tregistrar_conta
    l - \tlistar contas
    q - \tsair
    :: '''

def main():

    AGENCY = '0001'

    manage_account = Manage_Account()

    while True:

        try:
            option = input(menu())
            if option == 'd':
                nro = int(input('Digite o numero da conta: '))
                account = manage_account.get_account(nro)
                if account:
                    valor = float(input('Digite o valor de deposito: '))
                    if valor <= 0:
                        print('Valor invalido')
                    else:
                        manage_account.deposito(valor, account)
                        print(account.saldo)
                        print('deposito realizado')
            elif option == 's':
                nro = int(input('Digite o numero da conta: '))
                account = manage_account.get_account(nro)
                if account:
                    valor = float(input('Digite o valor de saque: '))
                    if valor <= 0:
                        print('Valor invalido')
                    elif not manage_account.exeder_limite(valor, account=account):
                        manage_account.saque(valor, account)
                        print('saque realizado')
                    elif account.saldo < valor and valor <= account.LIMITE_SAQUE:
                        print('Saldo insuficiente')
                    elif valor > account.LIMITE_SAQUE:
                        print('Excedido o limite de saque diario')
                    elif account.LIMITE_DIARIO > 3:
                        print('Excedido o quantidade de saque diario')
            elif option == 'e':
                nro = int(input('Digite o numero da conta: '))
                account = manage_account.get_account(nro)
                if account:
                    manage_account.extrato(account)
            elif option == 'r':
                cpf = input('Informe o cpf do cliente: ')
                client = manage_account.get_client(cpf)
                if client:
                    manage_account.account_register(AGENCY, client)
            elif option == 'c':
                nome = input('Digite o nome: ')
                cpf = input('Digite o cpf: ')
                endereco = input('Digite o endereco: ')
                manage_account.client_register(nome, cpf, endereco)
            elif option == 'l':
                manage_account.list_account()
            elif option == 'q':
                break
            else:
                print('Opcao invalida!')
            os.system('pause')
        except Exception as err:
            print('Error: ', err)

if __name__ == '__main__':
     main()
```

[class client](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Otimizando%20o%20Sistema%20Banc%C3%A1rio%20com%20Fun%C3%A7%C3%B5es%20Python/client.py)

```
class Client:
    def __init__(self, *, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco       
```
[class account](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Otimizando%20o%20Sistema%20Banc%C3%A1rio%20com%20Fun%C3%A7%C3%B5es%20Python/account.py)

```
class Account:

    LIMITE_DIARIO = 0
    LIMITE_SAQUE = 500

    def __init__(self, agency, client, nro):
        self.agency = agency
        self.nro = nro
        self.client = client
        self.saldo = 0
```

[class manager_account](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Otimizando%20o%20Sistema%20Banc%C3%A1rio%20com%20Fun%C3%A7%C3%B5es%20Python/manage_account.py)

```
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

    def client_register(self, nome, cpf, endereco):
        if not self.clients:
            self.clients.append(Client(nome=nome, cpf=cpf, endereco=endereco))
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
                print('NOME: '+account.client.nome, 'CC: '+str(account.nro), 'SALDO R$ - '+str(account.saldo))
        else:
            print('Nao ha contas cadastradas')

    def deposito(self, valor, account, /):
        account.saldo += round(valor,2)
        self.operacoes.append('NOME: '+account.client.nome+' CC:  '+str(+account.nro)+' DATA '+datetime.now().strftime('%d-%m-%Y - %H:%M')+' - deposito R$: '+str(valor))

    def saque(self, valor, account, /):
        account.saldo -= round(valor,2)
        account.LIMITE_SAQUE -= round(valor,2)
        account.LIMITE_DIARIO += 1
        self.operacoes.append('NOME: '+account.client.nome+' CC:  '+str(+account.nro)+' DATA '+datetime.now().strftime('%d-%m-%Y - %H:%M')+' - saque R$: '+str(valor))

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
```
