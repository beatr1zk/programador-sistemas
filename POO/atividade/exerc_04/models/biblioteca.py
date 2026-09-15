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
    def disponivel(self):
        return "Disponível" if self._disponivel else "Indisponível"

    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print (f"\nTítulo: {livro.titulo} \n| Autor: {livro.autor} \n| Ano: {livro.ano} \n| Disponibilidade: {livro.disponivel}\n\n---------------------------------------------------" )

    def emprestar(self):
        if self._disponivel:
            self._disponivel = False

    def devolver(self):
        if not self._disponivel:
            self._disponivel = True