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

### [Criando uma Lista de Equipamentos](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Dominando%20os%20Fundamentos%20B%C3%A1sicos%20do%20Python/criando_uma_lista_de_equipamentos.py)

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
### [Validando Número de Telefone](https://github.com/elnataoliveira/DIO/blob/main/Python%20AI%20Backend%20Developer/Desafios/Dominando%20os%20Fundamentos%20B%C3%A1sicos%20do%20Python/validando_numero_de_telefone.py)
```
# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
   
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = r"\(\d{2}\)\s9\d{4}-\d{4}"

    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):
      
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
      return "Número de telefone válido."
    else: 
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
      return "Número de telefone inválido." 
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)

```
