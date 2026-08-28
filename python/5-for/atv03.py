# Crie um vetor vazio que receberá do usuário o nome de 5 cidades utilizando for.
# Depois, utilize outro fo para exibir todas as cidades cadastradas

cidades: list[str] = []

print("\nDigite o nome de cinco cidades\n")

for i in range(5):
    print(f"Digite a {i+1}ª cidade:") 
    cidade = input("")
    cidades.append(cidade)

print("\nAqui estão todas as cidades enumeradas:")
for i in range(len(cidades)):
    print(f"{i+1} - {cidades[i]}")

# Jacarepaguá
# Piracicaba
# Ourinhos
# Porto de galinhas
# Goytacazes
    