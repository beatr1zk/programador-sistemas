class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade   
        self.ativo = False

pessoa1 = Pessoa("Amanda", "18")
pessoa2 = Pessoa("Any", "15")

pessoa = [pessoa1, pessoa2] 

print(f"{pessoa1.nome} tem {pessoa1.idade} anos")
print(f"{pessoa2.nome} tem {pessoa2.idade} anos")
