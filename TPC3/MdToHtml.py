
import sys
import re

def processa_titulo (linha):

    # Captura qualquer conteudo entre dois cardinais
    formula_titulo = re.compile(r'^(#+ )(.*?)$')
    
    # Substitui todas as ocorrencias com <hN>CONTEUDO</hN>
    #   Sendo N = len (match.group(1)) 
    #         CONTEUDO = match.group(2)
    #   
    #   E sendo match.group (1) => String com cardinais
    #           match.group (2) => Conteudo entre os cardinais

    linha = formula_titulo.sub(lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>" , linha)
    
    return linha


def processa_bold (linha):

    # Captura qualquer conteudo entre quatro asteriscos
    formula_bold = re.compile(r'\*{2}(.*?)\*{2}')

    # Substitui pelo formato abaixo
    # Sendo match.group (1) => Conteudo entre os asteriscos
    linha = formula_bold.sub (lambda m: f"<b>{m.group(1)}</b>", linha)
    
    return linha


def processa_italico (linha):

    # Captura qualquer conteudo entre dois asteriscos
    formula_italico = re.compile(r'\*{1}(.*?)\*{1}')

    # Substitui pelo formato abaixo
    # Sendo match.group (1) => Conteudo entre os asteriscos
    linha = formula_italico.sub (lambda m: f"<i>{m.group(1)}</i>", linha)
    
    return linha


def processa_lista_numerada (linha):
    
    # Variavel que determina se houve match
    mudou = False

    # Captura linha cujo inicio tenha um numero um ponto e um espaço
    formula_lista_numerada = re.compile(r'^\d+\. (.*)$')

    # Determina se linha segue o padrão
    match = formula_lista_numerada.match(linha)
    if match:

        # Match
        mudou = True

        # Se for o primeiro elemento da lista adiciona div inicial
        if (match.group(1) == "1"):
            linha = f"<ol>\n<li>{match.group(1)}</li>"

        # Senão utiliza o padrao seguinte
        else:
            linha = f"<li>{match.group(1)}</li>"

        # Sendo match.group (1) => Linha começando no caractere após o espaço
    
    return (linha, mudou)


def processa_link (linha):

    # Captura conteudo que siga o padrão [CONTEUDO](CONTEUDO)
    formula_link = re.compile(r'\[(.*?)\]\((.*?)\)')

    # Substitui pelo formato abaixo
    # Sendo match.group (1) => descrição do site encontrada entre os parenteses retos
    # Sendo match.group (1) => URL do site encontrado entre os parenteses
    linha = formula_link.sub (lambda m: f"<a herf=\"{m.group(2)}\">{m.group(1)}</a>", linha)
    
    return linha


def processa_imagem (linha):

    # Captura conteudo que siga o padrão ![CONTEUDO](CONTEUDO)
    formula_imagem = re.compile(r'\!\[(.*?)\]\((.*?)\)')

    # Substitui pelo formato abaixo
    # Sendo match.group (1) => descrição da imagem encontrada entre os parenteses retos
    # Sendo match.group (1) => caminho para a imagem encontrado entre os parenteses
    linha = formula_imagem.sub (lambda m: f"<img src=\"{m.group(2)}\" alt= \"{m.group(1)}\"/>", linha)
    
    return linha


def le_linha (linha, lista_numerada):

    # Retira \n
    linha = linha.strip()

    linha = processa_titulo (linha)
    linha = processa_bold (linha)
    linha = processa_italico (linha)
    linha = processa_link (linha)
    linha = processa_imagem(linha)
    (linha , mudou) = processa_lista_numerada(linha)

    # Se a ultima linha pertencia a uma lista e a atual não fechamos o div <ol> com </ol>
    if lista_numerada and not mudou:
        # Adiciona div de fecho á linha anterior á atual
        linha = "</ol>\n" + linha

    return (linha, mudou)


def main ():

    # 0 argumentos => Utiliza stdin
    if len (sys.argv) == 1:

        # Variavel que ajuda a determinar se a lista numerada acabou
        lista_numerada = False

        print ("Insira o texto linha a linha:")

        # Itera linha a linha pelo stdin
        for linha in sys.stdin:
            (string_output, lista_numerada) = le_linha (linha, lista_numerada)
            print (string_output)

    # 1 argumento => Utiliza argumento como caminho para ficheiro de input
    elif len (sys.argv) == 2:

        # Recebe argumento 1 => Caminho para ficheiro de input
        ficheiro = sys.argv [1]

        try: 
            # Tenta abrir ficheiro input
            texto = open (ficheiro , "r")

            # Cria e abre ficheiro output
            output = open ("resultado.txt", "w")

            # Variavel que ajuda a determinar se a lista numerada acabou
            lista_numerada = False

            # Percorre linhas do input
            for linha in texto:

                # Processa linha do input
                (string_output, lista_numerada) = le_linha (linha, lista_numerada)

                # Escreve output no ficheiro de output
                output.write(f"{string_output}\n")

        except FileNotFoundError:
            # Ficheiro não existe
            print ("Ficheiro de input não encontrado")

    else:
        print ("numero de argumentos incorreto")
        return
    

if __name__ == "__main__":
    main ()