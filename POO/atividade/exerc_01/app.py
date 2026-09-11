from models.alunos import Aluno

aluno_1 = Aluno("Diogo", "Administração", 18)
aluno_2 = Aluno("Daniel", "Análise e Desenvolvimento de Sistemas", 22)
aluno_3 = Aluno("Adrianna", "Design Gráfico", 27)
aluno_4 = Aluno("Samara", "Gastronomia", 24)
aluno_5 = Aluno("Chystopher", "Mecatrônica", 22)
aluno_6 = Aluno("Yasmin", "Medicina", 26)

def main():
    Aluno.listar_alunos()

if __name__ == '__main__':
    main()