from model.client import Client


class Client_Controller:
    def __init__(self):
        self._clients = []
    def client_register(self, name, cpf, date_of_birth, address):
        if not self._clients:
            self._clients.append(Client(name=name, cpf=cpf, date_of_birth=date_of_birth, address=address))
            print('Cliente cadastrado')
            print(self._clients[0].name)
        else:
            for client in self._clients:
                if client.cpf == cpf:
                    print('Cpf ja cadastrado')
                    break

    def get_client(self, cpf):
        if self._clients:
            for client in self._clients:
                if client.cpf == cpf:
                    return client
            print('Cliente nao cadastrado')
        else:
            print('Nao ha clientes cadastrados')

    @property
    def list_clients(self):
        return self._clients