# **Operadores e expressões em python**
========================================================
Em Python, operadores e expressões são utilizados para realizar operações sobre variáveis e valores. Os operadores permitem manipular dados de diferentes formas, enquanto as expressões combinam valores, variáveis e operadores para produzir novos valores.

## Tipo de operadores

### Aritiméticos

*   **Soma "+"**
`print(1 + 1)`
    >Saida: 2
***
*   **Subtração "-"**
`print(1 - 1)`
    >Saida: 0
***
*   **Divisão "/"**
`print(1 / 1)`
    >Saida: 1
***
*   **Divisão inteira "//"**
    `print(3 // 2)`
    > Saida: 1
***
*   **Multiplicação "*"**
    `print(2 * 2)`
    > Saida: 4
***
*   **Potencia ou exponencial " ** "**
    `print(2**3)`
    > Saida: 8
***
*   **Resto da divisão "%"**
    `print(5 % 2)`
    >Saída:  1

=====================================================
### Comparação

*   **Igual a "=="**
    `print(1 == 1)`
    >Saída: True
***
*   **Diferente de "!="**
    `print(1 != 1)`
    >Saída: False
***

*   **Maior e Menor que ">" e "<"**
    `print(1 > 1)`
    >Saída:  False
    
***

* **Maior igual e Menor igual a ">=" e "<="**
    `print(1 >= 1)`
    > Saída: True

=====================================================
### Lógicos

*   "and"
    Retorna True se ambas as expressões forem verdadeiras
    ```
    estudar  = True
    todo_dia = True

    if (estudar == True) and (todo_dia == True ):
        print("Sou muito estudante")
    else:
        print("Eu tenho preguiça, mas eu tento")
    ```
    > Saída: Sou muito estudante
***
*  **"or"**
    Retorna True se pelo menos uma das expressões for verdadeira
    ```
    musculação = True
    cardio     = True

    if (musculação == True) or (cardio == False):
        print('Eu vou emagrecer de qualquer forma')
    ```
    >Saída:  Eu vou emagrecer de qualquer forma
***
*   **"not"**
Inverte o valor lógico de uma expressão.
*Verificando se uma lista está vazia*
```
lista = []

if not lista:
    print("A lista está vazia.")
else:
    print("A lista não está vazia.")
```
Saída:  A lista está vazia.

=====================================================
### Atribuição

*   **Atribuição "="**
    Atribui um valor a uma variável
    ```
    x = 5
    nome = fulano
    ```
    > Saída: 5 e fulano

    ***
*   **Atribuição "+="**
    Atribui o valor de uma expressão e soma com o valor atual da variável
    ```
    x = 5
    x += 5
    ```
    >Saída:  x = 10
    ***
*   **Atribuição "-="**
    Atribui o valor de uma expressão e subtrai com o valor atual da variável
    ```
    x = 5
    x -= 5
    ```
    >Saída:  x = 0
    ***
*   **Atribuição "*="**
    Atribui o valor de uma expressão e multiplica com o valor atual da variável
    ```
    x = 5
    x *= 5
    ```
    > Saída:  x = 25
    ***
*   **Atribuição "/="**
    Atribui o valor de uma expressão e divide com o valor atual da variável
    ```
    x = 5
    x /= 5
    ```
    > Saída:  x = 1.0
=====================================================
### Associação

*   **"in"**
    Verifica se um valor está presente em uma lista ou string
    ```
    frutas = ['maçã', 'banana', 'laranja']
    print('maçã' in frutas)
    ```
    > Saída: True
    ***
*   **"not in"**
    Verifica se um valor não está presente em uma lista ou string
    ```
    frutas = ['maçã', 'banana', 'laranja']
    print('uva' not in frutas)
    ```
    > Saída: True