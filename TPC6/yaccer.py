from lexers import tokens
import ply.yacc as yacc
import sys

def p_inicio (token):
    'inicio : expressao'
    print (f"Resultado: {token[1]}")

def p_expressao_numero (token):
    'expressao : NUM'
    token [0] = token [1]

def p_expressao_soma (token):
    'expressao : expressao SOMA expressao'
    token[0] = token [1] + token [3]

def p_expressao_subtracao (token):
    'expressao : expressao SUB expressao'
    token[0] = token [1] - token [3]

def p_expressao_multiplicacao (token):
    'expressao : expressao MUL expressao'
    token[0] = token [1] * token [3]

def p_expressao_divisao (token):
    'expressao : expressao DIV expressao'
    token[0] = int (token [1] / token [3])

def p_expressao_parenteses (token):
    'expressao : PA expressao PF'
    token[0] = token[2]


def p_error (token):
    print (f"Erro na expressão: {token.value}")

precedence = (
    ('left', 'SOMA', 'SUB'),  # + e - têm a mesma prioridade (associam à esquerda)
    ('left', 'MUL'),  # * tem prioridade mais alta
    ('nonassoc', 'PA', 'PF')  # Parênteses não são associativos
)

parser = yacc.yacc()

def main():
    if len(sys.argv) != 2:
        print("Uso: python yaccer.py <caminho_para_ficheiro>")
        return

    caminho = sys.argv[1]


    try:
        with open(caminho, 'r', encoding='utf-8') as f:

            for line in f:
                parser.parse(line.strip())


    except FileNotFoundError:
        print(f"Erro: ficheiro '{caminho}' não encontrado.")

if __name__ == "__main__":
    main()