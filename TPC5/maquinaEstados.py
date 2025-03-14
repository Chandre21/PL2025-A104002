
import sys
import ply.lex
import json

# Variáveis globais
balance = 0
running = True
stock = []
coin_balance = 0

def calcular_troco(balance: float) -> str:
    # Definir o valor das moedas
    moedas = [2, 1, 0.5, 0.2, 0.1, 0.05]  # Moedas em euros
    troco = []

    # Calcular a quantidade de cada moeda
    for moeda in moedas:
        quantidade = int(balance // moeda)
        if quantidade > 0:
            if moeda >= 1:
                troco.append(f"{quantidade}x {int(moeda)}e")  # Moedas em euros
            else:
                troco.append(f"{quantidade}x {int(moeda*100)}c")  # Moedas em centavos
        balance -= quantidade * moeda

    # Formatar a string com "e" antes do último item, se houver mais de um item
    if len(troco) > 1:
        return ", ".join(troco[:-1]) + " e " + troco[-1]
    elif troco:
        return troco[0]

    return False


# Tokens
tokens = (
            'LISTAR',
            'MOEDAS',
            'SELECIONAR',
            'CODIGO',
            'NUMERO',
            'SAIR',
            'MOEDAEND'
         )


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


# Estados do Lexer
states = (
            ('InsercaoMoedas', 'exclusive'),
            ('SelecaoProduto', 'exclusive'),
         )      


# Funções Lexer
def t_LISTAR (token):
    r'LISTAR'

    print ("maq:")
    print ("cod | nome | quantidade | preço")
    print ("-------------------------------")

    global stock

    for item in stock:
        print (f"{item ['cod']}  {item ['nome']}  {item ['quant']}  {item ['preco']}")

    return token

def t_MOEDAS (token):
    r'MOEDA'
    token.lexer.begin('InsercaoMoedas')
    return token

def t_SELECIONAR (token):
    r'SELECIONAR'
    token.lexer.begin('SelecaoProduto')
    return token

def t_SAIR (token):
    r'SAIR'
    global balance
    troco = calcular_troco (balance)
    if troco != False:
        print (f"maq: Pode retirar o troco: {troco}")
    print ("maq: Até à próxima")


    global running
    running = False
    return token    

def t_InsercaoMoedas_NUMERO (token):
    r'1e|2e|5c|10c|20c|50c'

    global coin_balance

    if 'e' in token.value:
        coin_balance += int(token.value[:-1])
    else:
        coin_balance += int(token.value[:-1]) / 100

    coin_balance = round (coin_balance, 2)

    return token

def t_InsercaoMoedas_MOEDAEND (token):
    r'.'
    global balance
    global coin_balance

    balance += coin_balance
    coin_balance = 0

    coin_balance = round (balance, 2)

    balance_inteiro = int (balance)
    balance_n_inteiro = int(round((balance - balance_inteiro) * 100))

    print (f"maq: Saldo = {balance_inteiro}e{balance_n_inteiro}c")

    token.lexer.begin('INITIAL')
    return token

def t_SelecaoProduto_CODIGO (token):
    r'[A-Z]\d+'

    global balance

    for item in stock:
        if item ['cod'] == token.value :
            if item ['preco'] <= balance:

                # Efetua compra
                item ['quant'] = item ['quant'] - 1
                balance -= item ['preco']

                balance = round (balance, 2)
                print (f"maq: Pode retirar o produto dispensado \"{item ['nome']}\"")

                balance_inteiro = int (balance)
                balance_n_inteiro = int(round((balance - balance_inteiro) * 100))

                print (f"maq: Saldo = {balance_inteiro}e{balance_n_inteiro}c")

                token.lexer.begin('INITIAL')
                return token

            else:
                print ("maq: Saldo insufuciente para satisfazer o seu pedido")

                balance_inteiro = int (balance)
                balance_n_inteiro = int(round((balance - balance_inteiro) * 100))

                preco = item ['preco']
                preco_inteiro = int (preco)
                preco_n_inteiro = int(round((preco - preco_inteiro) * 100))

                print (f"maq: Saldo = {balance_inteiro}e{balance_n_inteiro}c; Pedido = {preco_inteiro}e{preco_n_inteiro}c")

                token.lexer.begin('INITIAL')
                return token      

    print (f"maq: Não existe um artigo com código: {token.value}")
    token.lexer.begin('INITIAL')
    return token

def t_error(token):
    print(f"Caractere inválido: {token.value[0]}")
    token.lexer.skip(1)

def t_InsercaoMoedas_error(token):
    print(f"Caractere inválido: {token.value[0]}")
    token.lexer.skip(1)

def t_SelecaoProduto_error(token):
    print(f"Caractere inválido: {token.value[0]}")
    token.lexer.skip(1)

def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_SelecaoProduto_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_InsercaoMoedas_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)


# Criar Lexer
global tokenizer
tokenizer = ply.lex.lex()


# Main
def main ():
    print ("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print ("maq: Bom dia. Estou disponível para atender o seu pedido.")

    global stock
    with open('stock.json', 'r', encoding='utf-8') as file:
        stock = json.load(file)

    for line in sys.stdin:
        if not line:
            continue  # Passar à frente linhas vazias

        global tokenizer
        tokenizer.input(line)

        with open('tokens.log', 'w', encoding='utf-8') as file:
            for token in tokenizer:
                file.write(str(token) + '\n')

        # tokenizer = ply.lex.lex()  # Apagar tokens do lexer

        if not running:
            break

    with open('stock.json', 'w', encoding='utf-8') as file:
        json.dump(stock, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()