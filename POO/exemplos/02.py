class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade   
        self.ativo = False
    def __str__(self):
        # return self.nome
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos"

pessoa1 = Pessoa("Amanda", "18")
pessoa2 = Pessoa("Any", "15")

pessoa = [pessoa1, pessoa2]

print(pessoa1)
print(pessoa2)

