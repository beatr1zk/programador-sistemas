from models.biblioteca import Livro

livro_1 = Livro("Corte de Espinhos e Rosas", "Sarah J. Maas", 2015)
livro_2 = Livro("Trono de Vidro", "Sarah J. Maas", 2012)
livro_3 = Livro("Assistente do Vilão", "Hannah Nicole Maehrer", 2023)
livro_4 = Livro("Heartstopper: Dois Garotos, Um Encontro", "Alice Oseman", 2016)
livro_5 = Livro("Berserk", "Kentaro Miura", 1989)

Livro.emprestar(livro_1)
Livro.emprestar(livro_2)

Livro.devolver(livro_2)

def main():
    Livro.listar_livros()

if __name__ == '__main__':
    main()