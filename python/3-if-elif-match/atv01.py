print("\nPara verificar se sua compra é elegível para o desconto de 10%, insira o valor abaixo:\n")

valor= float(input("Insira o valor da compra: "))

if valor >= 200:
    valor_desconto = valor * 0.1
    valor_final = valor - porcen
    print(f"\nO valor da sua compra com desconto aplicado é R${valor_final:.2f}. O valor do desconto é R${valor_desconto:.2f} do valor original da sua compra.")

else:
    print("\nSua compra não atingiu o valor mínimo de R$200.\n")