# PL2025-A104002

## De:
- **Nome:** André Barbosa Teixeira
- **Número de aluno:** A104002

## Trabalho Para Casa Semana 1 ##

### Problema ###
1. Pretende-se um programa que some todas as sequências de digitos que encontre num texto.
2. Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado
3. Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado
4. Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída

### Solução ###
O programa abre e determina se recebeu um argumento na sua invocação. Se o tiver recebido tentará utiliza-lo como caminho para o ficheiro de texto. Se não utilizará o stdin.

O programa irá dividir o texto em linhas e cada uma será processada separadamente.

O processamento de uma linha é feito caráter a caráter e está dividido em três partes:
1. Independente do estado: Procura o caráter "=". Se o encontrar envia a soma atual para a saída.
2. Apenas executado se o estado é igual a ON: Procura digitos e a sequencia "Off"
3. Apenas executado se o estado é igual a OFF: Procura a sequencia "On"

## Utilização ##
O programa pode ser executado de duas formas:
1. Utilizando Stdin como input de texto.
    ```sh
    $ python Somador.py
    ```
2. Utilizando um ficheiro como input de texto.
    ```sh
    $ python Somador.py <caminho_para_ficheiro>
    ```
