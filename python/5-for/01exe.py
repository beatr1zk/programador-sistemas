#==============================================================================
# EXPLICAÇÃO:

# for → indica que vamos repetir algo.
# i → é a variável que recebe cada valor.
# in → significa "dentro de".
# range → gera os valores do range

# for i in range → Repita o código, fazendo i assumir os valores que estão dentro de range().

#==============================================================================

print("\n# O for pode utilizar seu contador como índice do vetor")

alunos: list[str] = ["Rapunzel", "Flin", "Gothel"]

for i in range(len(alunos)):
    print(alunos[i])  

#==============================================================================

print("\n# Podemos mostrar o índice junto com o valor.")

frutas: list[str] = ["Maça", "Banana", "Banga"]

for i in range(len(frutas)):
    print(f"Índice: {i}")
    print(f"Fruta: {frutas[i]}")

#===============================================================================

print("\n# O índice começa em zero, mas podemos apresentar uma numeração começando em um")

produtos: list[str] = ["Borboleta", "Pichurucu", "Pinto"]

for i in range (len(produtos)):
    print(i + 1, "-", produtos[i])

print("# O índice continua sendo i, mas a numeração exibida i + 1.")

#===============================================================================

print("\n# Você pode também inserir um valor para mostrar junto ao indice com input")

nomes: list[str] = []

for i in range (5):
    nome = input("Digite um nome: ")
    print(i+1, "-", nome)
    nomes.append(nome)
print(nomes)

#===============================================================================

print("\n# Cadastrar e depois listar")

alunos: list[str] = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    print(i+1, "-", nome)
    alunos.append(nome)

    print("===== ALUNOS =====")

    for i in range (len(alunos)):
        print(i+1, "-", alunos[i])

print("# O primeiro laço cadastra os valores. O segundo laço exibe os valores cadastrados")

#===============================================================================

print("\n# Um contador pode registrar quantos elementos atendam uma condição")

idades: list[int] = [15, 19, 18, 21, 12, 30]

maiordeidade = 0

for i in range(len(idades)):
    if (idades[i] >= 18):
        maiordeidade += 1

print(f"Maiores de idade: {maiordeidade}")

#===============================================================================

print("\n# A pesquisa sequencial verifica os elementos por um até encontrar o valor desejado")


nomes: list[str] = ["Nicolas", "Gustavo", "Paulo"]

pesquisa = "Bruno"
encontrado = False

for i in range(len(nomes)):
    if (nomes[i] == pesquisa):
        encontrado = True

print(f"Encontrado {pesquisa}")

#===============================================================================

print("\n# Depois de encontrar o elemento, não precisa continuar pesquisando. Então podemos usar BREAK")

for i in range(len(nomes)):
    if (nomes[i] == pesquisa):
        posicao = i
        print(posicao)
        break

#===============================================================================

print("\n# Encontrando o maior valor")

# considere
numeros: list[int] = [8, 9, 15, 6, 10]

# Começamos considerando que o primeiro elemento é o maior 
maior = numeros[0]

# Depois comparamos os demais:
for i in range(len(numeros)):
    if (numeros[i] > maior):
        maior = numeros[i]

print(f"O maior valor é o {i-1}º número → {maior}")




