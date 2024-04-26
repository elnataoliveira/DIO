## Criando um Sistema Bancário com Python

### - [Função main](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Criando%20um%20Sistema%20Banc%C3%A1rio%20com%20Python/main.py)

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

### - [Class model](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Criando%20um%20Sistema%20Banc%C3%A1rio%20com%20Python/conta.py)
```
from datetime import datetime

class Conta:

    LIMITE_DIARIO = 0
    LIMITE_SAQUE = 500

    def __init__(self, nro_conta, saldo):
        self.nro_conta = nro_conta
        self.saldo = round(saldo,2)
        self.operacoes = []

    def deposito(self, valor):
        self.saldo += round(valor,2)
        self.operacoes.append(datetime.now().strftime('%d-%m-%Y - %H:%M')+' - depostivo - '+str(valor))

    def saque(self, valor):
        self.saldo -= round(valor,2)
        self.LIMITE_SAQUE -= round(valor,2)
        self.LIMITE_DIARIO += 1

        self.operacoes.append(datetime.now().strftime('%d-%m-%Y - %H:%M')+' - saque - '+str(valor))

    def extrato(self):
        if len(self.operacoes) == 0:
            print('Nao foram realizadas movimentacoes')
        else:
            for operacao in self.operacoes:
                print(operacao)
            print('Saldo - ' + str(round(self.saldo,2)))

    def exeder_limite(self, valor):
        if self.saldo < valor:
            return True
        elif self.LIMITE_DIARIO > 3:
            return True
        elif valor > self.LIMITE_SAQUE:
            return True
        else:
            return False
```
