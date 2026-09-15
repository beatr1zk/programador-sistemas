class Livro:
    livros = []

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._disponivel = True
        
        Livro.livros.append(self)

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Ano: {self.ano}"

    @property
    def disponibilidade(self):
        return "Disponível" if self._disponivel else "Indisponível"

    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print (f"\nTítulo: {livro.titulo} \n| Autor: {livro.autor} \n| Ano: {livro.ano} \n| Disponibilidade: {livro.disponibilidade}\n\n---------------------------------------------------" )

    def emprestar(self):
        self._disponivel = not self._disponivel

    def devolver(self):
        if self._disponivel == False:
            self._disponivel = True
        else:
            return self._disponivel