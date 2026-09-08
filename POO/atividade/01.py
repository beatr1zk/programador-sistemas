class Produto:
    produtos = []
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco   
        self.disponivel = False
    def __str__(self):
        return f"Produtos: {self.nome} - R${self.preco}"

produto01 = Produto("detergente", 12.99)
produto02 = Produto("heron", 0.25)
produto03 = Produto("computaria", 1.456)

print (produto01)
print (produto02)
print (produto03)