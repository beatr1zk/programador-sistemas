from models.conta_bancaria import ContaBancaria

conta_1 = ContaBancaria("Diogo", 1000)
conta_2 = ContaBancaria("Adrianna", 500)

print("\nEscolha sua conta: \n1 - Diogo \n2 - Adrianna\n")

conta_escolhida = int(input("Digite o número da conta escolhida: "))

match conta_escolhida:
    case 1:
        conta = conta_1

    case 2:
        conta = conta_2

    case _:
        print("Conta inválida")
        conta = None

while True:
    menu(conta)

    print("\nDeseja continuar?")
    continuar = input("Selecione uma opção s/n: ")

    if continuar == "n":
        break