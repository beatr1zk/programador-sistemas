# Crie um vetor que contenha uma lista de nomes (Frodo, Samwise, Gandalf, Merry, Pippin), depois utilize o for para exibir

nomes: list[str] = ["Frodo", "Samwise", "Gandalf", "Merry", "Pippin"]


for i in range (len(nomes)):
    print(i+1, "-", nomes[i])

# TRADUÇÃO for i in range (len(nomes)):
# para cada nome¹ no intervalo² da lista de nomes³ leia cada um da seguinte forma⁴:

# ¹ nome = i
# ² intervalo = range
# ³ lista de nomes = (len(nomes)
# ⁴ da seguinte forma = :


# TRADUÇÃO print(i+1, "-", nomes[i]):

# print() → imprima o que está entre ()
# i → verifica qual a posição está o do nome: P0, P1, P2... 
# +1 → adiciona + 1 no valor do (i)índice, que anteriormente era 0, e passa a ser 1 (0 + 1 = 1), e assim sucessivamente 1 + 1 = 2
# "-" → adiciona um risco (-) ao imprimir, para separar o número do nome
# nomes → acessa a lista de nomes
# [i] → verifica dentro dessa lista a posição que cada nome ocupa e imprime 1 por 1 em ordem


