
import sys
import Musica

def ler_linha (linha):


    num_colunas = 7

    strings = []
    while num_colunas > 0:
        aspas = 0        

        num_colunas -= 1

    nome = strings [0]
    descricao = strings [1]
    anoCriacao = strings [2]
    periodo = strings [3]
    compositor = strings [4]
    duracao = strings [5]
    id = strings [6]



    musica = Musica (nome, descricao, anoCriacao, periodo, duracao, id)
    return musica





def main ():

    # Verifica se um caminho de ficheiro é passado ao executar o programa
    if len (sys.argv) != 2 :
        print ("Numero de argumentos incorreto")
        return 1

    # Recebe caminho de ficheiro do terminal
    ficheiro = sys.argv [1]

    #* read_csv

    # Criar lista de musicas
    lista_de_musicas = []

    # Tenta abrir ficheiro em modo leitura
    try:
        texto = open (ficheiro, "r")

        # Itera pelas linhas do ficheiro
        for linha in texto:
            nova_musica = ler_linha (linha)
            lista_de_musicas.append (nova_musica)

    except FileNotFoundError:
        print ("Ficheiro não encontrado")

    
    


    #* sortcsv



if __name__ == "__main__":
    main ()