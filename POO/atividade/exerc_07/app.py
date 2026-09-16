from models.alunos import Aluno
from models.cursos import Curso

sistemas = Curso("Desenvolvedor de sistemas")
web = Curso("Programador Web")


sistemas.matricular_aluno("Bia", 18)
sistemas.matricular_aluno("João", 20)

web.matricular_aluno("Maria", 19)
web.matricular_aluno("Pedro", 21)

def main():
    sistemas.listar_alunos()
    web.listar_alunos()

if __name__ == '__main__':
    main()