import ply.lex as lex

tokens = ['NUM', 'SOMA', 'SUB', 'MUL', 'DIV', 'PA', 'PF']

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

lexer = lex.lex()

