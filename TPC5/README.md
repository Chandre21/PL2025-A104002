# PL2025-A104002

## De:
![](foto2.png)
- **Nome:** André Barbosa Teixeira
- **Número de aluno:** A104002

## Trabalho Para Casa Semana 5 ##

### Problema ###
Deseja-se construir uma maquina de estados para simular uma maquina de vending.

### Solução ###
O programa abre e o utilizador pode usar o terminal para enviar instruções como "LISTAR", "SELECIONAR A23" e outros para operar a máquina de vending. As instruçoes são capturadas e processadas linah a linha utilizando um **lexer**.


#### Procura de padões ####
Existe um conjunto de tokens:

```py
tokens = (
            'LISTAR',
            'MOEDAS',
            'SELECIONAR',
            'CODIGO',
            'NUMERO',
            'SAIR',
            'MOEDAEND'
         )
```

```py
# Expressões regulares
t_LISTAR = r'LISTAR'
t_MOEDAS = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_CODIGO = r'[A-Z]\d+'
t_NUMERO = r'(1e|2e|5c|10c|20c|50c)'
t_SAIR = r'SAIR'
t_MOEDAEND = r'.'

t_ignore = ' \t'
t_InsercaoMoedas_ignore = ' \t'
t_SelecaoProduto_ignore = ' \t'
```

Estas são usadas em funções começadas por **t_** que serão reconhecidas pelo (ply.lex) lexer chamado aqui de **tokenizer**.

Exemplo de função do lexer:
```py
def t_InsercaoMoedas_NUMERO (token):
    r'1e|2e|5c|10c|20c|50c'

    global coin_balance

    if 'e' in token.value:
        coin_balance += int(token.value[:-1])
    else:
        coin_balance += int(token.value[:-1]) / 100

    coin_balance = round (coin_balance, 2)

    return token
```


O tokenizer será responsavel por receber as linhas do stdin e utilizar as várias funções definidas para encontrar padrões e retirar informação e agir como esperado.

## Utilização ##
```sh
    $ python maquinaEstados.py
```

Os comandos disponiveis são:

    1.LISTAR
    2.MOEDA
    3.SELECIONAR
    4.SAIR
