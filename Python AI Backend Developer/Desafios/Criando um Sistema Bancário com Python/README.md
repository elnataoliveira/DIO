## Criando um Sistema Bancário com Python

```
import os
from model.conta import Conta

def gerir_conta():

    conta = Conta(nro_conta=123, saldo=0)
    options = '''Digite uma opcao:
    
d - depositar
s - sacar
e - extrato
q - sair
==> '''

    while True:

        try:
            option = input(options)
            if option == 'd':
                valor = float(input('Digite o valor de deposito: '))
                if valor <= 0:
                    print('Valor invalido')
                else:
                    conta.deposito(valor)
                    print('deposito realizado')
            elif option == 's':
                valor = float(input('Digite o valor de saque: '))
                if valor <= 0:
                    print('Valor invalido')
                elif not conta.exeder_limite(valor):
                    conta.saque(valor)
                    print('saque realizado')
                elif conta.saldo < valor and valor <= conta.LIMITE_SAQUE:
                    print('Saldo insuficiente')
                elif valor > conta.LIMITE_SAQUE:
                    print('Excedido o limite de saque diario')
                elif conta.LIMITE_DIARIO > 3:
                    print('Excedido o quantidade de saque diario')
            elif option == 'e':
                conta.extrato()
            elif option == 'q':
                break
            else:
                print('Opcao invalida!')
            os.system('pause')
            os.system('cls')
        except Exception as err:
            print('Error: ', err)

if __name__ == '__main__':

     gerir_conta()
```
