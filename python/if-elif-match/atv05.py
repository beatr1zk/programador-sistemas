print("\nOpções:")
print("1 = cadastrar")
print("2 = consultar")
print("3 = excluir\n")

opcao=int(input("Digite um número para selecionar uma opção: "))

match opcao:
    case 1:
        print("\nCadastrar")
    case 2:
        print("\nConsultar")
    case 3:
         print("\nExcluir")
    case _:
        print("\nOpção inválida")
