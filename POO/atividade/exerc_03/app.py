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

if conta:
    print("\nQual operação deseja realizar? \n1 - Consultar saldo \n2 - Depositar \n3 - Sacar")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print(f"Seu saldo é: R$ {conta.saldo:.2f}")

        case 2:
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
            print(f"Novo saldo: R$ {conta.saldo:.2f}")

        case 3:
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
            print(f"Novo saldo: R$ {conta.saldo:.2f}")

        case _:
            print("Opção inválida")

if conta:
    print(conta)

def main():
    ContaBancaria.listar_contas()

if __name__ == '__main__':
    main()