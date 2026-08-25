# Crie um algoritmo que calcule a média da turma, onde o usuário irá informar quais foram as notas dos alunos após realizará o calculo da média da turma

quantidade = int(input("Quantos alunos há na turma? "))
soma = 0

for i in range(quantidade+1):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota

media = soma / quantidade

print("A média da turma é:", media)