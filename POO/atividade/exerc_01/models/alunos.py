class Aluno:
    alunos = []

    def __init__(self, nome_aluno, curso, idade):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.idade = idade

        Aluno.alunos.append(self)

    def __str__(self):
        return f"Nome: {self.nome_aluno} Curso: {self.curso} Idade: {self.idade}"

    @classmethod
    def listar_alunos(cls):
        for aluno in cls.alunos:
            print(f"\nNome: {aluno.nome_aluno} \n|Curso: {aluno.curso} \n|Idade: {aluno.idade} \n \n\n---------------------------------------------------")
            