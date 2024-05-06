import os

class Menu:

    def menu(self):
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


    def interface(self, checking_account_controller, client_controller):
        while True:

            try:
                option = input(self.menu())
                if option == 'd':
                    number = int(input('Digite o numero da conta: '))
                    account = checking_account_controller.get_account(number)
                    if account:
                        value = float(input('Digite o valor de deposito: '))
                        if value <= 0:
                            print('Valor invalido')
                        elif checking_account_controller.is_deposited(value, account):
                            print('SALDO R$ - '+str(account.sold))
                            print('deposito realizado')
                        else:
                            print(checking_account_controller.is_deposited(value, account))

                elif option == 's':
                    number = int(input('Digite o numero da conta: '))
                    account = checking_account_controller.get_account(number)
                    if account:
                        value = float(input('Digite o valor de saque: '))
                        if value <= 0:
                            print('Valor invalido')
                        elif not checking_account_controller.exceed_limit(value, account=account):
                            checking_account_controller.is_withdrew(value, account)
                            print('saque realizado+')
                        elif account.sold < value and value <= account.withdraw_limit:
                            print('Saldo insuficiente')
                        elif value > account.withdraw_limit:
                            print('Excedido o limite de saque diario')
                        elif account.daily_limit < 1:
                            print('Excedido o quantidade de saque diario')
                elif option == 'e':
                    number = int(input('Digite o numero da conta: '))
                    account = checking_account_controller.get_account(number)
                    if account:
                        checking_account_controller.bank_statment(account)
                elif option == 'r':
                    cpf = input('Informe o cpf do cliente: ')
                    client = client_controller.get_client(cpf)
                    if client:
                        checking_account_controller.account_register(client, client_controller)
                elif option == 'c':
                    name = input('Digite o nome: ')
                    cpf = input('Digite o cpf: ')
                    date_of_birth = input('Digite a data de nascimento: ')
                    address = input('Digite o endereco: ')
                    client_controller.client_register(name, cpf, date_of_birth, address)
                elif option == 'l':
                    checking_account_controller.list_account()
                elif option == 'q':
                    break
                else:
                    print('Opcao invalida!')
                os.system('pause')
            except Exception as err:
                print('Error: ', err)