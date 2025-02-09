import sys


def ler_linha(linha, estado, soma):

    posicao_leitor = 0

    # Iterar pelos characteres da linha
    while len (linha) > posicao_leitor:

        # Encontra um =
        if linha [posicao_leitor] == "=":
            print (f"Resultado atual: {soma}")
            posicao_leitor += 1

        #* Estado ON

        elif estado == 1 :

            # Encontra um numero
            if linha [posicao_leitor] in "0123456789":
                numero = int (linha [posicao_leitor])
                posicao_leitor += 1

                # Itera pelos characteres enquanto pertencerem ao numero
                while len (linha) > posicao_leitor and linha [posicao_leitor] in "0123456789":
                    numero = numero * 10 + int (linha [posicao_leitor])
                    posicao_leitor += 1
                
                soma += numero
        
            # Encontra um OFF
            elif len (linha) >= posicao_leitor + 2 and linha [posicao_leitor] in "oO":
                if linha [posicao_leitor + 1] in "fF" and linha [posicao_leitor + 2] in "fF":
                    estado = 0
                    posicao_leitor += 2

                posicao_leitor += 1
            
            # Não encontra nada
            else:
                posicao_leitor += 1

        
        #* Estado OFF

        else:

            # Encontra um ON
            if len (linha) >= posicao_leitor + 1 and linha [posicao_leitor] in "oO":
                if linha [posicao_leitor + 1] in "nN":
                    estado = 1
                    posicao_leitor += 1

            posicao_leitor += 1


    return (soma, estado)


def main ():
    estado = 0  # 0 será equivalente a OFF e 1 a ON
    soma = 0

    #* Determina se foi recebido um caminho para ficheiro

    if len (sys.argv) > 1 :

        # Recebe caminho de ficheiro do terminal
        ficheiro = sys.argv [1]

        # Tenta abrir ficheiro
        try:
            texto = open (ficheiro, "r")

            # Itera pelas linhas do ficheiro
            for linha in texto:
                (soma, estado) = ler_linha (linha, estado, soma)

        except FileNotFoundError:
            print (f"erro a abrir ficheiro")
        
    #* Nao foi dado um caminho para um ficheiro na invocação do programa => vai ser usado o stdin

    else:
        print ("Estado inicial é OFF. Insira o texto:")

        # Itera pelas linhas do stdin
        for linha in sys.stdin:
            (soma, estado) = ler_linha (linha, estado, soma)


    #* Acabou a leitura
    print (f"Leitura terminada. Resultado: {soma}")

    return soma

if __name__ == "__main__":
    main()