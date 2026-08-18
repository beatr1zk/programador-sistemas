print("\nPara exibir a sua média preciso que preencha as informações abaixo\n")

nome=input("Insira o seu nome: ")
n1=float(input("\nInsira sua 1ª nota: "))
n2=float(input("Insira sua 2ª nota: "))
n3=float(input("Insira sua 3ª nota: "))

media=(n1+n2+n3)/3

print("\n", nome, f"esta é a média das suas notas: {media:.2f} \n")