print("\nSaboes:")
print("1 = Carne")
print("2 = Queijo")
print("3 = Vento")
print("4 = Pizza\n")

opcao = int(input("Selecione um sabor de pastel: "))

match opcao:
    case 1:
        print("Pastel de carne")
    case 2:
        print("Pastel de queijo")
    case 3:
        print("Pastel de vento")
    case 4:
        print("Pastel sabor pizza")
    case _:
        print("Escolha uma opção válida!")