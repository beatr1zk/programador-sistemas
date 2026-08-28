# Para acessar um elemento usamos dois índices: linha(x) e coluna(y)
# A sintaxe é: matriz [linha] [coluna]

numeros: list[list[int]] = [
    [10, 20, 30], # linha 0
    [40, 50, 60], # linha 1
    [70, 80, 90] # linha 2
] #   0   1   2  → colunas

print("\nProcurando um valor determinado:")
print(numeros[0][0]) #10 → linha 0, coluna 0
print(numeros[1][2]) #60 → linha 1, coluna 1

# EXEMPLO:
# numeros[0][0] → Resultado: 10
# numeros[1][2] → Resultado: 60
# numeros[2][0] → Resultado: 70

# ----------------------------------------------------------------------------------------------------------------------------

# ALTERANDO UM VALOR DA MATRIZ:

# Matriz original (antes)
numeros: list[list[int]] = [
    [10, 20],
    [30, 40]
]

print("\nAntes:")
print(numeros[0]) # [10, 20]
print(numeros[1]) # [30, 40]

# Vamos alterar o valor da posição [1][0]

numeros[1][0] = 100
# valor alterado: 30 → 100

# Matriz alterada (depois)
numeros: list[list[int]] = [
    [10, 20],
    [100, 40]
]

print("\nDepois:")
print(numeros[0]) # [10, 20]
print(numeros[1]) # [100, 40]

# numeros [linha][coluna] = novo valor

# ----------------------------------------------------------------------------------------------------------------------------

# QUANTIDADE DE LINHAS E COLUNAS
# Para descobrir quantas linhas uma matriz possui, usamos a propriedade lenght

print("\nQuantidade de linhas na matriz:")
num_linhas = len(numeros)
print(num_linhas)

print("\nQuantidade de colunas na matriz:")
num_colunas = len(numeros[0])
print(num_colunas)

# ----------------------------------------------------------------------------------------------------------------------------

# PERCORRENDO UMA LINHA COM FOR
# Podemos usar um for para percorrer todos os elementos de uma linha específica

# TRADUÇÃO: para cada índice dentro do intervalo do tamanho da linha
for col in range(len(numeros[0])):
    print(numeros[0][col]) # Saída: 10, 20, 30

# numeros[0] acessa a primeira linha. O for percorre cada coluna dessa linha.

# ----------------------------------------------------------------------------------------------------------------------------
