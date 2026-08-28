# Crie um algoritmo que calcule a média da turma, onde o usuário irá informar qual foi a nota do aluno e caso não tenha nenhuma nota ele poderá 
# encerrar o programa e solicitar o resultado de média

calcular_notas = True
media = 0
contador = 0

while calcular_notas:
    print("\n1 - para adicionar notas")
    print("2 - sair\n")
    opcao = int(input("Digite uma opção entre 1 e 2: "))

    if opcao == 1:
        nota = float(input("Digite a nota do aluno: "))
        media += nota
        contador = contador + 1

    elif opcao == 2:
        print("\n. ݁₊ ⊹ . ݁ 𐙚 ݁ . ⊹ ₊ ݁.\n")
        print("Saindo, até mais!")
        print(f"Média da turma de {contador} alunos é {media/contador:.2f}\n")
        calcular_notas = False 

    else:
        print("Digito inválido!")

    