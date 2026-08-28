# Crie um vetor com cinco produtos

# Utilize um for para exibir todos os produtos em uma lista numerada

# Ao final, mostre: Total de produtos 5

produtos: list[str] = ["Disjuntor bipolar", "Bucha S10", "Lâmpada de ozônio", "Silicone acético"]

for i in range (len(produtos)):
    # print (i+1, "-", produtos[i])
    print (f"{i+1} - {produtos[i]}")

print(f"\nTotal de produtos: {len(produtos)}")

