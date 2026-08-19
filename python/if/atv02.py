print("\nPara descobrir se tem saldo suficiente em sua conta, preencha as informações: \n")

saldo=float(input("Valor disponível na sua conta: "))
saque=float(input("Valor a ser sacado: "))

if saldo >= saque:
    resto = saldo - saque
    print(f"\Saque autorizado, o saldo atual da conta é: R${resto}")

else:
    print("\nSaque não autorizado, saldo insuficiente\n")
    