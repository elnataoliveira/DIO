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



