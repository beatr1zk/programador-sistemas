class Pessoa:
    pessoas = []

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade   
        self.ativo = False
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos"
    
    def listar_pessoas():
        for i in Pessoa.pessoas:
            print(f"Pessoa: {i.nome}, {i.idade} anos")

pessoa1 = Pessoa("Amanda", "18")
pessoa2 = Pessoa("Any", "15")

Pessoa.listar_pessoas()