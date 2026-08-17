print ("\nCalcula seu IMC:\n")

peso = float(input("Digite o seu peso(Kg):"))
altura = float(input("Digite sua altura(M):"))

formula = peso / (altura*altura)

print("\nSeu IMC é:", formula, "\n")

print("| IMC            | Classificação      |")
print("| -------------- | ------------------ |")
print("| Menor que 18,5 | Abaixo do peso     |")
print("| 18,5 a 24,9    | Peso normal        |")
print("| 25 a 29,9      | Sobrepeso          |")
print("| 30 a 34,9      | Obesidade grau I   |")
print("| 35 a 39,9      | Obesidade grau II  |")
print("| 40 ou mais     | Obesidade grau III |")










