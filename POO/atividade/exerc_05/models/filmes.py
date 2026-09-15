class Filme:
    filmes = []

    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        
        Filme.filmes.append(self)

    def __str__(self):
        return f"Título: {self.titulo} | Gênero: {self.genero} | Ano: {self.ano}"

    @classmethod
    def listar_filme(cls):
        for filme in cls.filmes:
            print (f"\nTítulo: {filme.titulo} \n| Gênero: {filme.genero} \n| Ano: {filme.ano} \n\n---------------------------------------------------" )