# Crie um vetor vazio chamado compras 

# solicite ao usuário três produtos e adicione-os utilizando append()

# Ao final exiba:

# ==== LISTA DE COMPRAS ====
# Produtos:
# Quantidade de produtos:
# Primeiro produto:
# Último produto:

continuar = True
compras = []

print("\nDigite sua lista de compras (digite 'fim' para encerrar): \n")

while continuar == True:
    produto = input("Digite um produto: ")

    compras.append(produto)

    if compras[len(compras)-1] == "fim":
        continuar = False
        compras.pop()

print("\n==== LISTA DE COMPRAS ====\n")
print(f"Produtos: {compras}")
print(f"Quantidade de produtos: {(len(compras))}")
print(f"O primeiro produto é: {compras[0]}")
print(f"O último produto é: {(compras[len(compras)-1])}\n")

