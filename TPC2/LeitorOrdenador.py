
import sys
import os
from Musica import Musica


def le_texto (texto):

    # Numero de colunas do csv
    num_colunas = 7
    coluna_atual = 0

    # Criar lista de palavras
    strings = []
    string = ""

    # Variavel para determinar se ta dentro de aspas (1 dentro, 0 fora)
    aspas = 0

    # Criar lista de musicas
    lista_de_musicas = []

    # Remover primeira linha
    for linha in texto:
        break

    # Por cada linha
    for linha in texto:
    
        posicao_leitor = 0
        # Ler todos os carateres da linha
        while len(linha) > posicao_leitor:

            # Caso obtenha um ";" que nao esteja entre aspas (acabou uma das colunas)
            if (linha [posicao_leitor] == ";" or linha [posicao_leitor] == "\n") and aspas == 0:

                strings.append(string)
                string = ""
                coluna_atual += 1

                if coluna_atual == num_colunas:

                    nova_musica = Musica (strings [0], strings [1], strings [2], strings [3], strings [4], strings [5], strings [6])

                    lista_de_musicas.append (nova_musica)
                    strings = []
                    coluna_atual = 0

            elif linha [posicao_leitor] == "\n":
                pass
            
            else: 
                # Insere caratere na coluna (/palavra)
                string += linha [posicao_leitor]

                if linha [posicao_leitor] == "\"":
                    if aspas == 1:
                        aspas = 0
                    else:
                        aspas = 1

            posicao_leitor += 1

    # fim do while (EOF) mete a ultima linha
    strings.append(string)
    string = ""
    coluna_atual += 1

    if coluna_atual == num_colunas:

        nova_musica = Musica (strings [0], strings [1], strings [2], strings [3], strings [4], strings [5], strings [6])

        lista_de_musicas.append (nova_musica)
        strings = []
        coluna_atual = 0

    return lista_de_musicas

def ordenar_por_compositor (lista_de_musicas):
    
    # Cria lista ordenada
    musicas_ordenadas = sorted(lista_de_musicas, key=lambda m: m.compositor.lower())

    with open ("resultados/ordenada_por_compositor.txt", "w", encoding="utf-8") as output1:

        # Print da lista ordenada
        for musica in musicas_ordenadas:
            output1.write (str(musica) + "\n")

def distribuir_por_periodo (lista_de_musicas):
    
    # Cria dicionario
    periodo_num = {}

    # Percorre lista de musicas
    for musica in lista_de_musicas:

        # Se nao existir ainda periodo, cria key no dicionario e mete valor 1
        if not musica.periodo in periodo_num:
            periodo_num [musica.periodo] = 1

        # Se já existe adiciona 1 (musica atual)
        else:
            periodo_num [musica.periodo] += 1

    with open ("resultados/distribuicao_por_periodo.txt", "w", encoding="utf-8") as output2:

        # Print descrição
        output2.write (f"Periodo:    Numero de musicas\n\n")
        
        # Print dicionario
        for key, value in periodo_num.items():
            output2.write (f"{key}:    {value}\n")

def dicionario_lista_ordenada (lista_de_musicas):

    # Cria dicionario
    periodo_lista = {}

    # Percorre todas as musicas e adiciona ao dicionario por periodo
    for musica in lista_de_musicas:

        # Se nao existir ainda periodo, cria key no dicionario
        if not musica.periodo in periodo_lista:
            periodo_lista [musica.periodo] = []
        
        # Adiciona musica atual ao dicionario na respetiva key
        periodo_lista [musica.periodo].append(musica)

    # Percorre dicionario
    for key, value in periodo_lista.items():

        # Para cada key ordena lista de musicas pelo nome
        periodo_lista [key] = sorted(value, key=lambda m: m.nome.lower())

    with open ("resultados/dicionario_lista_ordenada.txt", "w", encoding="utf-8") as output3:
        
        # Print do dicionario
        for key, value in periodo_lista.items():
            output3.write (f"{key}:\n")
            for music in value:
                # Print de apenas o nome da musica
                output3.write (f"   {music.nome};\n")

def main ():

    # Verifica se um caminho de ficheiro é passado ao executar o programa
    if len (sys.argv) != 2 :
        print ("Numero de argumentos incorreto")
        return 1

    # Recebe caminho de ficheiro do terminal
    ficheiro = sys.argv [1]

    #* Ler csv

    # Criar lista de musicas
    lista_de_musicas = []

    # Tenta abrir ficheiro em modo leitura
    try:
        texto = open (ficheiro, "r", encoding="utf-8")

        # Itera pelas linhas do ficheiro
        lista_de_musicas = le_texto(texto)

    except FileNotFoundError:
        print ("Ficheiro não encontrado")

    #* Resultados

    os.makedirs("resultados", exist_ok=True)

    #* Ordenar por compositor

    ordenar_por_compositor (lista_de_musicas)

    #* Distribuição por periodo

    distribuir_por_periodo (lista_de_musicas)

    #* Dicionario com lista ordenada

    dicionario_lista_ordenada (lista_de_musicas)
    

if __name__ == "__main__":
    main ()