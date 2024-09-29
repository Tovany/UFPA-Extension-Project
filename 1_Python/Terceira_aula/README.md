# Tipos de dados
=================================================================

## O que são tipos de dados?
Em Python, um tipo de dado define o tipo de valor que uma variável pode armazenar. Cada tipo de dado tem suas próprias características e operações que podem ser realizadas sobre ele.

### Os tipos de dados são:

#### 1. Numéricos
int: `inteiro = 10`
float: `flutuante = 1.90`
complex: `imaginario = 1 + 2j`

=================================================================

#### 2. Sequencias
##### 2.1 string

> Cadeira de caracteres
```string = "Meu nome é Marcos"
print(f"Tipo de dado: {type(string)}")
```
***
##### 2.2 Lista
> Coleção ordenada e multável de itens. Pode conter itens de diferentes tipos:
```
lista = ["joão", "Rafaela", "Igor", 1, 23, 10, 0.1]
print(f'Tipo de dado: {type(lista)}')
```
***
##### 2.3 tuple
> Coleção ordenada e imutável de itens. Pode conter intes de diferentes tipos também
```
tuple = (.1, 1, 2, 4, 5, "Paralelepipedo")
print(f'Tipo de dado: {type(tuple)}')
```
***
##### 2.4 range
> Sequencia numérica

```
sequencia = range(10)
print(f'Tipo de dado: {type(sequencia)}')
```
=================================================================
#### 3. Mapeamento

##### 3.1 Dicionário
Um dicionário em Python é uma estrutura de dados que armazena pares de chave-valor.

```
nomes = ["Fulano", "Ciclano"]
idades = [10, 20]
dicionario = {"Nomes": nomes, "Idades": idades}
print(f'Tipo de dado {type(dicionario)}')

> importando uma biblioteca chamada pandas para criar um dicionário

import pandas as pd
pd.DataFrame(dicionario)
```
***

##### 3.2 Booleano
Representa os valores de verdadeiro ou falso

```
Verdadeiro = True
Falso = False
print(f'O valor Verdadeiro corresponde a {int(Verdadeiro)}')
print('')
print(f'O valor falso corresponde a {int(Falso)}')
```
=====================================================================
#### Exercicio
* Métodos construtores
> Métodos construtores são funções especiais que são utilizadas para criar instâncias de classes ou converter valores entre tipos diferentes. Em Python, esses métodos são chamados para inicializar um objeto de uma determinada classe.

> Os métodos construtores são:

```
int()
float()
str()
bool()
```
> Mas, como utilizar esses métodos? Esse é sua tarefa. Descubra como usar os métodos construtores para conversão dos valores, como de float para int ou até mesmo de numéricos para strings.

> Você pode usar a internet, chat GPT, GEMINI, colar do colegar, não tem probrema, o importante é tentar fazer. **OBS:Não cole nas provas kkk**

> Se quiserem, façam grupos.

> Já foi usado nos exemplos acima métodos construtores, então, se você achar, você já tem uma pista de como usar.

[Link para o código da aula](https://github.com/Tovany/extensaoUFPA/blob/develop/1_Python/Terceira_aula/1_Data_types_code.py)