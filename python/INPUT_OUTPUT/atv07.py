print("\nCalcule o preço de determinada quantidade de um produto")

produto=input("\nNome do produto: ")
preco=float(input("Preço do produto: "))
qnt=int(input("Quantidade do produto: "))

compra = preco * qnt

print(f"\nA compra total do produto foi de {compra:.2f} \n")