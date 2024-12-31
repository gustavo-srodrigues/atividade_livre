class Livro:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano


livro1 = Livro("o nome do vento", 2009)

print(f'{livro1.titulo} e data de publicação: {livro1.ano}')