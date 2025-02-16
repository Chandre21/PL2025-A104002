
class Musica:

    def __init__(self, nome, descricao, anoCriacao, periodo, compositor, duracao, id):
        self.nome = nome
        self.descricao = descricao
        self.anoCriacao = anoCriacao
        self.periodo = periodo
        self.compositor = compositor
        self.duracao = duracao
        self.id = id

    def __str__(self):
        return (f"Musica {self.id}:\nNome: {self.nome}\nAno: {self.anoCriacao}\nPeriodo: {self.periodo}\nCompositor: {self.compositor}\nDuração: {self.duracao}\nDescrição: {self.descricao}\n")