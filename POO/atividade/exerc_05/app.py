from models.filmes import Filme

filme_1 = Filme("O Senhor dos Anéis: A Sociedade do Anel", "Peter Jackson", 2001)
filme_2 = Filme("Harry Potter e a Pedra Filosofal", "Chris Columbus", 2001)
filme_3 = Filme("Coraline", "Henry Selick", 2009)
filme_4 = Filme("A Viagem de Chihiro", "Hayao Miyazaki", 2001) 
filme_5 = Filme("Interestelar", "Christopher Nolan", 2014)

def main():
    Filme.listar_filme()

if __name__ == '__main__':
    main()