class personagem:
    def __init__(self, nome, descricao, imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.programa = programa
        self.animador = animador

    def __str__(self):
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nImagem: {self.imagem}\nPrograma: {self.programa}\nAnimador: {self.animador}"       