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
                manage_account.client_register(nome, cpf)
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
