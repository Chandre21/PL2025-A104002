# PL2025-A104002

## De:
- **Nome:** André Barbosa Teixeira
- **Número de aluno:** A104002

## Trabalho Para Casa Semana 2 ##

### Problema ###
1. Pretende-se criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet.
    1. Lista ordenada alfabeticamente dos compositores musicais;
    2. Distrinuição das obras por período: quantas obras catalogadas em cada período;
    3. Dicionário em que a cada período está associada uma lista alfabética dos títulos desse período.

### Solução ###

O programa abre e determina se recebeu um argumento na sua invocação. Se o tiver recebido tentará utiliza-lo como caminho para o ficheiro de texto. Se não, utilizará o stdin como input.

O programa irá dividir o texto em linhas e analisará essas linhas utilizando 6 funções auxiliares:

1.processa_titulo
2.processa_bold
3.processa_italico
4.processa_lista_numerada
5.processa_link
6.processa_imagem

Cada uma destas funções tratará de procurar na linha recebida um padrão de sintaxe MarkDown e substitui-lo pela sintaxe HTML equivalente.

#### Procura de padões ####

Para procurar facilmente os padrões de sintaxe necessários para a tradução, foi utilizada a biblioteca **RE**.

Padrões utilizados:
1. Captura de titulos.
    ```
    Exemplo:
        In: # Exemplo
        Out: <h1>Exemplo</h1>

    Padrão utilizado: r'^(#+ )(.*?)$'
    ```
2. Captura de texto **bold**.
    ```sh
    Exemplo:
        In: Este é um **exemplo** ...
        Out: Este é um <b>exemplo</b> ...

    Padrão utilizado: r'\*{2}(.*?)\*{2}'
    ```
3. Captura de texto *italico*.
    ```sh
    Exemplo:
        In: Este é um *exemplo* ...
        Out: Este é um <i>exemplo</i> ...

    Padrão utilizado: r'\*{1}(.*?)\*{1}'
    ```
4. Captura de listas numeradas.
    ```sh
    Exemplo:
        In: 1. Primeiro item
            2. Segundo item
            3. Terceiro item
        Out: <ol>
             <li>Primeiro item</li>
             <li>Segundo item</li>
             <li>Terceiro item</li>
             </ol>

    Padrão utilizado: r'^\d+\. (.*)$'
    ```
5. Captura de links.
    ```sh
    Exemplo:
        In: Como pode ser consultado em [página da UC](http://www.uc.pt)
        Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

    Padrão utilizado: r'\[(.*?)\]\((.*?)\)'
    ```
6. Captura de imagens.
    ```sh
    Exemplo:
        In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
        Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...

    Padrão utilizado: r'\!\[(.*?)\]\((.*?)\)'
    ```

## Utilização ##
O programa pode ser executado de duas formas:
1. Utilizando Stdin como input de texto.
    ```sh
    $ python MdToHtml.py
    ```
2. Utilizando um ficheiro como input de texto.
    ```sh
    $ python MdToHtml.py <caminho_para_ficheiro>
    ```

Caso seja escolhido o segundo metodo, os resultados serão guardados no ficheiro **resultado.txt**
