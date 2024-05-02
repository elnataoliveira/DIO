## Dominando os Fundamentos Básicos do Python

### [Verificador de Planos de Internet](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Dominando%20os%20Fundamentos%20B%C3%A1sicos%20do%20Python/desafio.py)

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
