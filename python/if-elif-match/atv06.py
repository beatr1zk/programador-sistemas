print("\nEscolha o dia da sua consulta:")
print("2 = segunda")
print("3 = terça")
print("4 = quarta")
print("5 = quinta")
print("6 = sexta\n")                                

opcao=int(input("De segunda a sexta: "))

match opcao:
    case 2:
        print("\nConsulta agendada para segunda-feira! Nos vemos lá!")

    case 3:
        print("\nConsulta agendada para terça-feira! Nos vemos lá!")

    case 4:
         print("\nConsulta agendada para quarta-feira! Nos vemos lá!")

    case 5:
         print("\nConsulta agendada para quinta-feira! Nos vemos lá!")

    case 6:
         print("\nConsulta agendada para sexta-feira! Nos vemos lá!")

    case _:
        print("\nOpção inválida")