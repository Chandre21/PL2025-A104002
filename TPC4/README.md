# PL2025-A104002

## De:
![](foto2.png)
- **Nome:** André Barbosa Teixeira
- **Número de aluno:** A104002

## Trabalho Para Casa Semana 4 ##

### Problema ###
Deseja-se construir um analisador léxico para uma liguagem de query.

### Solução ###
O programa abre um ficheiro especificado utilizador. Posteriormente ele divide o texto em linhas e analisa-as através da função `analisa_linha` que utiliza expressões regulares para encontrar padrões.

#### Token ####
Para armazenar os elementos encontrados no texto foi criada a classe **Token**.
```py
class Token:
    tipo : str  # Tipo de match
    valor : str  # Conteudo do match
    linha : int   # Linha em que o match foi encontrado
    posicao : int  # Posiçao do match na linha
```

#### Procura de padões ####
É criado um conjunto de expressões regex `padroes_tokens` definida como:
```py
padroes_tokens = [
    ('COMENTARIO', r'#.*'),
    ('NUMERO', r'\d+'),
    ('CHAVETAS', r'[{}]'),
    ('DOISPONTOS', r':'),
    ('PREFIXO', r'\w+(?=:)'),
    ('SUFIXO', r'(?<=:)\w+'),
    ('VARIAVEL', r'\?[\w]+'),
    ('PALAVRA', r'"[^"]*"'),
    ('PALAVRA-CHAVE', r'[a-zA-Z]+\b'),
    ('LINK', r'@[a-zA-Z]+'),
    ('PONTO-FINAL', r'\.'),
    ('SKIP', r'[\s\t]+'),
    ('ERRO', r'.')
]
```

Este conjunto de expressões é posteriormente utilizado todo em cunjunto na expressão regex:

```py
regex_total = '|'.join(f'(?P<{nome}>{regex})' for nome, regex in padroes_tokens)
```

Os valores dos mathces são armazenados numa lista de `Tokens` que são posteriormente imprimidos no ficheiro de output **resultado.txt**.


## Utilização ##
Para executar o programa usamos o seguinte comando, sendo **<file_name>** o caminho para o ficheiro .csv com o texto a converter.
```sh
    $ python AnalisadorLexico.py <file_name>
```

Os resultados das ordenações e agrupamentos das listas serão inseridos em ficheiros .txt na pasta **resultados**
