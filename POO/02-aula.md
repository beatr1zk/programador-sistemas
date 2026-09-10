# Objetivo da aula:
- Aprender o que é '@property' para controlar como um atributo é lido.
- O que são atributos protegidos como '_underscore' e por que proteger dados.
- '@classmethod' a diferença entre métodos de classes e de instância.
- Como separar o projeto em multiplos arquivos usando import (repasse de informações entre arquivos).
- Criação de novas classes e relacionar com outros arquivos.
- Como exibir média formatada no terminal.

**-------------------------------------------------------------------------------------------------------------------------------------**

# @property (exemplo 04, L 21)

Transforma um método em algo que se comporta como um atributo (sem usar '()')
Permite controlar como um valor é exibido ou calculado na hora da leitura (funciona como um tradutor)

Para fazer isso vamos criar uma função. Com nome de ativo, e adicionar o @property

- Exemplo de uso: em vez de mostrar 'True' / 'False' para 'Ativo' ou exibir um emoji indicando o status
  
    @property
    def ativo(self):
        return 'Inativo' if self._status else 'Ativo'

Além de alterar também os elementos de exibição que antes estavam como *.status* para *.ativo*

**-------------------------------------------------------------------------------------------------------------------------------------**

# @classmethod (exemplo 04, L 16)

Indica um método pertencente a classe, não a uma instância específica
Usa cls no lugar de 'self' como primeiro parâmetro

Exemplo de uso: 'listar_restaurante()' vira um '@classmethod', usando 'cls' em vez do nome fixo da classe

@classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:

**-------------------------------------------------------------------------------------------------------------------------------------**

# Exemplo real de separação (exemplo_final)

**-------------------------------------------------------------------------------------------------------------------------------------**


