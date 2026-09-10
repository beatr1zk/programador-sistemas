# O que é POO?

*POO (Programação Orientada a Objetos)* é um paradigma de programação que organiza o código a partir de *objetos*. Esses objetos representam elementos do mundo real ou conceitos do sistema e possuem *características (atributos)* e *ações (métodos)*.

Por exemplo, em um sistema de uma loja, podemos ter um objeto **Produto**, que possui atributos como nome e preço, e métodos como cadastrar, alterar ou excluir.

A POO ajuda a deixar o código mais **organizado, reutilizável e fácil de manter**, principalmente em sistemas maiores.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Classes?

Na Programação Orientada a Objetos (POO), as classes são utilizadas como *modelos ou estruturas para criar objetos*. Elas definem quais características e comportamentos esses objetos terão.

Uma classe pode possuir *atributos*, que representam as características de um objeto, e *métodos*, que representam as ações que ele pode realizar.

Por exemplo, podemos criar uma classe chamada "Carro". Nela, podemos definir atributos como **marca, modelo e cor**, além de métodos como **acelerar, frear e buzinar**.
A partir dessa classe, podemos criar vários objetos diferentes. Cada objeto terá seus próprios valores, mas seguirá a estrutura definida pela classe.

Dessa forma, as classes permitem *organizar, reutilizar e facilitar a manutenção do código*, sendo um dos principais conceitos da Programação Orientada a Objetos.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é o __init__ e o self?

**init** = é o método construtor. Roda automaticamente quando o objeto é criado. Garante que todo objeto já nasça com os atributos preenchidos (NOT NULL)
**self** = é o primeiro parâmetro de qualquer método de instância e representa o primeiro obejeto. Analogia: assim como passamos parâmetros para uma função. Passamos valor para o construtor

Uma classe SEMPRE deve começar comletra maiúscula

**-------------------------------------------------------------------------------------------------------------------------------------**

# Esta é a forma mais tosca de utilizar: (exemplo 01)

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

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é a função __str__? (exemplo 02)

A função str funciona como um retorno de mensagem padrão, como vemos nesse exemplo:

def __str__(self):
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos"

podemos também utilizar apenas return self.nome, que irá apenas retornar o nome

Depois, uma vez que usamos print(pessoa1), ele automaticamente retorna essa mensagem padrão do __str__, sem ter a necessidade de colar vários prints com o mesmo texto ficando dessa maneira:

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

retorno do print: Olá, eu sou Amanda, tenho 18 anos

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é a função listar? (exemplo 03)

Podemos criar uma função de lista para que toda vez que chamemos essa classe listar_pessoas(), assim, toda vez que executamos a classe ela puxa o for i in range para executar

def listar_pessoas():
        for i in Pessoa.pessoas:
            print(f"Pessoa: {i.pessoas}. Categoria: {i.idade}")

Pessoa.listar_pessoas()

*Em uma situação real:*
class Pessoa:
     pessoas = []  <-- Utilizamos essa função para criar a lista -->

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade   
        self.ativo = False
        Pessoa.pessoas.append(self)  <-- Utilizamos append para adicionar o self a lista que criamos -->

    def __str__(self):
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos"
    
    def listar_pessoas():
        for i in Pessoa.pessoas: 
            print(f"Pessoa: {i.pessoas}. Categoria: {i.idade}")

pessoa1 = Pessoa("Amanda", "18")
pessoa2 = Pessoa("Any", "15")

Pessoa.listar_pessoas()

**-------------------------------------------------------------------------------------------------------------------------------------**

# Momento atividade, criação de um modelo do 0, atividades 1 e 2