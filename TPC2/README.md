# PL2025-A104002

## De:
- **Nome:** André Barbosa Teixeira
- **Número de aluno:** A104002

## Trabalho Para Casa Semana 2 ##

### Problema ###
1. Pretende-se um programa que deverá ler o dataset, processá-lo e criar os seguintes resultados:
    1. Lista ordenada alfabeticamente dos compositores musicais;
    2. Distrinuição das obras por período: quantas obras catalogadas em cada período;
    3. Dicionário em que a cada período está associada uma lista alfabética dos títulos desse período.

### Solução ###

#### Parsing do ficheiro csv ####

O programa abre e determina se recebeu um argumento na sua invocação. Se o tiver recebido tentará utiliza-lo como caminho para o ficheiro de texto. Se não informa o utilizador que o numero de argumentos não é apropriado

O programa irá dividir o texto em linhas e posteriormente em carateres que serão processados individualmente.

No processamento de carateres encontramos apenas 2 carateres que não serão guardados nas strings que ficarão com a informação. Estes são:
1. "\n"
2. ";" apenas se estiver fora de aspas

As strings são construidas até ser encontrado um ";" (fora de aspas) e são posteriormente guardadas numa classe **Musica** que por sua vez são inseridas numa **lista de musicas**.

```py
class Musica:
    nome : str
    descricao : str
    anoCriacao : str
    periodo : str
    compositor : str
    duracao : str
    id : str
```

A lista de musicas é depois utilizada para obter todos os resultados requiridos pelo problema.

## Utilização ##
Para executar o programa usamos o seguinte comando, sendo **<file_name>** o caminho para o ficheiro .csv com a informação das musicas.
```sh
    $ python LeitorOrdenador.py <file_name>.csv
```

Os resultados das ordenações e agrupamentos das listas serão inseridos em ficheiros .txt na pasta **resultados**


