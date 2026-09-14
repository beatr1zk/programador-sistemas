# Objetivo da aula: 
- Organização de pastas e arquivos em projetos Python.
- Criação e utilização de classes base e classes derivadas.
- Herança entre classes.
- Reutilização do construtor da classe mãe com `super()`.
- Relacionamento entre diferentes classes.
- Refatoração e reutilização de métodos.
- Uso de `isinstance()` para verificar tipos de objetos.
- Uso de `@property` para acessar métodos como propriedades.
- Uso de `hasattr()` para verificar a existência de atributos ou métodos.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é uma herança? *exemplos/restaurante/models/cardapio*

Herança é um recurso da Programação Orientada a Objetos que permite que uma classe herde características e comportamentos de outra classe.

- A classe que fornece os recursos é chamada de classe mãe (superclasse).
- A classe que recebe esses recursos é chamada de classe filha (subclasse).
- Permite reaproveitar código, evitando repetições, além de possibilitar que a classe filha tenha suas próprias características e comportamentos.



# Como ela funciona?

A herança funciona quando uma classe filha recebe automaticamente os atributos e métodos de uma classe mãe. Para isso, a classe filha é definida indicando qual classe ela irá herdar.

A classe filha pode utilizar os recursos herdados, adicionar novos atributos e métodos ou até mesmo sobrescrever comportamentos da classe mãe.

O super() é utilizado para acessar a classe mãe, principalmente para reaproveitar seu construtor e evitar repetir código.

*Classe mãe*
class ItemCardapio:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

*Classe filha*
from cardapio.itemcardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco) *<- classe mãe sendo inserida*
        self.tamanho = tamanho

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é o isinstance()?

É uma função do Python usada para verificar se um objeto pertence a uma determinada classe ou a uma classe que herda dela.

Ele retorna True quando o objeto é daquela classe e False quando não é.
É muito útil para identificar o tipo de objeto antes de executar determinada ação, principalmente quando trabalhamos com herança e diferentes tipos de objetos.



# Como ela funciona?

def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

Nesse código, o isinstance() está sendo usado para *verificar se o item recebido pertence* à classe ItemCardapio ou a alguma classe que herda dela.

* item → objeto que está sendo passado para o método.
* ItemCardapio → classe que será usada para fazer a verificação.
* isinstance(item, ItemCardapio) → verifica se *item* é um *ItemCardapio*, 'Prato', 'Bebida', etc.
* Se for, o item é adicionado à lista *_cardapio* usando *append()*.

Ou seja, a ideia é **garantir que somente itens válidos do cardápio sejam adicionados à lista**.
