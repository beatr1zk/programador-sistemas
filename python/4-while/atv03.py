# Crie um algoritmo que faça uma contagem crescente de 1 até 20 exibindo somente os números pares

num = 0

while num <= 20:
    print (num)
    num += 2


num = 1

while num <= 20:
    if num % 2 == 0:
        print(num)

    num += 1