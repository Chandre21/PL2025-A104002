import sys
import re

class Token:
    def __init__(self, tipo, valor, linha, posicao):
        self.tipo = tipo
        self.valor = valor
        self.linha = linha
        self.posicao = posicao

    def __repr__(self):
        return f"{self.tipo} => \"{self.valor}\" (L:{self.linha}, C:{self.posicao})"

def analisa_linha (linha, num_linha):

    padroes_tokens = [
        ('COMENTARIO', r'#.*'),
        ('NUMERO', r'\d+'),
        ('CHAVETAS', r'[{}]'),
        ('DOISPONTOS', r':'),
        ('PREFIXO', r'\w+(?=:)'),
        ('SUFIXO', r'(?<=:)\w+'),
        ('VARIAVEL', r'\?[\w]+'),
        ('PALAVRA', r'"[^"]*"'),
        ('PALAVRACHAVE', r'[a-zA-Z]+\b'),
        ('LINK', r'@[a-zA-Z]+'),
        ('PONTOFINAL', r'\.'),
        ('SKIP', r'[\s\t]+'),
        ('ERRO', r'.')
    ]

    regex_total = '|'.join(f'(?P<{nome}>{regex})' for nome, regex in padroes_tokens)

    tokens = []

    for match in re.finditer(regex_total, linha):
        tipo = match.lastgroup
        valor = match.group()

        if tipo != 'SKIP':  # Ignorar espaços
            tokens.append(Token(tipo, valor, num_linha, match.start()))

    return tokens


def main ():

    # Numero errado de argumentos
    if len (sys.argv) > 2 :
        print ("numero de argumentos incorreto")
        return

    # Recebe argumento 1 => Caminho para ficheiro de input
    ficheiro = sys.argv [1]

    try: 
        # Tenta abriror len (sys.argv) != 1 ficheiro input
        with open(ficheiro, "r", encoding="utf-8") as texto, open("resultado.txt", "w", encoding="utf-8") as output:

            # Cria e abre ficheiro output
            output = open ("resultado.txt", "w")

            num_linha = 1

            # Percorre linhas do input
            for linha in texto:

                # Processa linha do input
                tokens = analisa_linha (linha , num_linha)

                # Escreve output no ficheiro de output
                for token in tokens :
                    output.write(f"{token}\n")

                num_linha += 1

    except FileNotFoundError:
        # Ficheiro não existe
        print ("Ficheiro de input não encontrado")
    

if __name__ == "__main__":
    main ()
