# Tipos de dados

# Numéricos
inteiro = 10  # int
flutuante = 1.90  # float
imaginario = 1 + 2j  # complex

# Sequencias
string = "Meu nome é Marcos"
print(f"Tipo de dado: {type(string)}")  # nova função

lista = ["joão", "Rafaela", "Igor", 1, 23, 10, 0.1]
print(f'Tipo de dado: {type(lista)}')

tuple = (.1, 1, 2, 4, 5, "Paralelepipedo")
print(f'Tipo de dado: {type(tuple)}')

sequencia = range(10)
print(f'Tipo de dado: {type(sequencia)}')

# Mapeamento
nomes = ["Fulano", "Ciclano"]
idades = [10, 20]

dicionario = {"Nomes": nomes, "Idades": idades}
print(f'Tipo de dado {type(dicionario)}')

import pandas as pd
pd.DataFrame(dicionario)

# Booleano
Verdadeiro = True
Falso = False

print(f'O valor Verdadeiro corresponde a {int(Verdadeiro)}')
print('')
print(f'O valor falso corresponde a {int(Falso)}')