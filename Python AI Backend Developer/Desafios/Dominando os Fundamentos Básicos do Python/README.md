## Dominando os Fundamentos Básicos do Python

### [Verificador de Planos de Internet](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Dominando%20os%20Fundamentos%20B%C3%A1sicos%20do%20Python/verificador_de_planos_de_internet.py)

```
# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
  plano = 'Plano Essencial Fibra - 50Mbps'
  if consumo > 10 and consumo < 20:
    plano = 'Plano Prata Fibra - 100Mbps'
  elif consumo > 19:
    plano = 'Plano Premium Fibra - 300Mbps'
# TODO: Retorne o plano de internet adequado:
  return plano
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
```

### [Criando uma Lista de Equipamentos]
(https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Dominando%20os%20Fundamentos%20B%C3%A1sicos%20do%20Python/criando_uma_lista_de_equipamentos.py)

```
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicita os itens ao usuário:
for i in range(3):
# TODO: Solicite o item e armazena na variável "item":
  item = input()
# TODO: Adicione o item à lista "itens":
  itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
```
