# PL2025-A104002

## De:
![](foto2.png)
- **Nome:** André Barbosa Teixeira
- **Número de aluno:** A104002

## Trabalho Para Casa Semana 6 ##

### Problema ###
Deseja-se construir um parser de expressões matemáticas

### Solução ###
O utilizador fornece um ficheiro com as expressões matemáticas ao programa. Este depois le o ficheiro e utilizando o lexer capta todos os diferentes tokens.
Estes sao depois passados ao yacc que utiliza recursividade para fazer o caminho de tokens singulares até ao resultado da expressão inteira.


#### Procura de padões ####
Existe um conjunto de tokens:

```py
tokens = (
            'NUM',
            'SOMA',
            'SUB',
            'MUL',
            'DIV',
            'PA',
            'PF'
         )
```

```py
# Expressões regulares
t_PA = r'\('
t_PF = r'\)'
t_SOMA = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_ignore = " \t\n"

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

```

O tokenizer será responsavel por receber as linhas do stdin e utilizar as várias funções definidas para encontrar padrões e retirar informação e agir como esperado.

#### YACC ####
O yacc recebe os tokens do lexer e vai recursivamente com os valores dos tokens calcular o valor final de cada expressão. 

Exemplo: 
```py
    def p_expressao_parenteses (token):
        'expressao : PA expressao PF'
        token[0] = token[2]
```
O valor "expressão" é retornado através da variavel token[0] que funciona como um return da função.
Este valor é o que depois será obtido se for acessado com token [*INDICE_NA_EXPRESSAO*].

## Utilização ##
Para executar o programa, escrevemos as expressões num ficheiro de texto e passamos o seu caminho, **<path_to_file>**, na chamada do programa como em seguida demonstrado: 

```sh
    $ python yaccer.py <path_to_file>
```
