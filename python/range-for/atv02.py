# Crie um algoritmo que realize a tabuada do número inserido pelo usuário

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)