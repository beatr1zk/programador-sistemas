# O que é um vetor? também chamado de array, é uma estrutura que permite armazenar vários valores dentro de uma única variável.

# Exemplos:
alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
numeros = ["3", "9", "7.6", "6.9", "10"]

# Agora todos os valores estão armazenados dentro da string alunos ou numeros, e são organizados da seguinte forma:
# Ana = P0        |     3 = P0
# Bruno = P1      |     9 = P1
# Carlos = P2     |     7.6 = P2
# Daniela = P3    |     6.9 = P3
# Eduardo = P4    |     10 = P4

# Para mostrar os valores da lista:

print(alunos[4]) 
# TRADUÇÃO: imprimir da lista "alunos" o valor 04 = "Eduardo"

print(numeros[2]) 
# TRADUÇÃO: imprimir da lista "numeros" o valor 02 = "7.6"

# ----------------------------------------------------------------------------------------------------------------------------

# Não é a forma mais usada mas ainda sim é possível indicar o tipo dos valores que serão armazenados. 

nomes: list[str] = ["Ana", "Bruno", "Carlos"]
notas: list[int] = [5, 7, 9]
numeros: list[float] = [8.9, 2.3, 9.9]
boolean: list[bool] = [True, False]

# A tipagem ajuda a evitar que valores incompatíveis sejam adicionados ao vetor.

# ----------------------------------------------------------------------------------------------------------------------------

# Também podemos alterar um valor já armazenado.

alunos: list[str] = ["Ana", "Beatriz", "Carlos"]

alunos[1] = "Bianca"

print(alunos)
# O resultado será Ana, Bianca e Carlos, pois o índice 1 foi substituido.

# ----------------------------------------------------------------------------------------------------------------------------

# O que é a propriedade len? Ela informa a quantidade de elementos do vetor.

frutas: list[str] = ["Maça", "Banana", "Laranja"]

print(len(frutas))
# Resultado: 3

# O vator possui três elementos

# ----------------------------------------------------------------------------------------------------------------------------

# O que é a propriedade append? O método append() adiciona um elemento no final do vetor.

nomes: list[str] = ["Alice", "João"]

nomes.append("Pedro")

print(nomes)
# Resultado: Alice, João, Pedro

# ----------------------------------------------------------------------------------------------------------------------------

# O que é o método Insert? o método insert adiciona um elemento na posição escolhida do vetor.print

nomes: list[str] = ["Tamlin", "Lucien"]

nomes.insert(0, "Feyre")

print(nomes)
# Resultado: Feyre, Tamlin, Lucien

# ----------------------------------------------------------------------------------------------------------------------------

# O que é o método pop? O método pop() remove o último elemento do vetor.

nomes: list[str] = ["Elain", "Nesha", "Alis"]

nomes.pop()
print(nomes)
# Resultado: Elain, Nesha

# ----------------------------------------------------------------------------------------------------------------------------

# O que é o método remove? O método remove() faz a remoção da primeira ocorrência de um valor específico dentro do vetor.

nomes: list[str] = ["Heron", "Chrys", "Willy"]

nomes.remove("Heron")

print(nomes)
# Resultado: Chrys, Willy