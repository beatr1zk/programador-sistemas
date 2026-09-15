# Objetivo da aula:
- Sala de aula invertida
- Dinâmica para compreender
  
**-------------------------------------------------------------------------------------------------------------------------------------**

# Com base nesses tópicos 
- IsInstance
- Hasattr
- Enumerate

*responda as perguntas abaixo respectivamente:*
1. O que é?
2. Como funciona no código
3. Uma analogia

**-------------------------------------------------------------------------------------------------------------------------------------**

# IsInstance

*1. O que é:*
Verifica se o item pertence a determinada instancia, retorna true ou false


*2. Como funciona no código:*
```python
if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
```

Se item for uma instância de (ItemCardapio) *<-- v/f*
    Adicione-o ao _cardapio


*3. Uma analogia:*
Em uma festa que só permite a entrada de pessoas que têm um ingresso VIP.
A pessoa chega na porta e o segurança pergunta: "Você é VIP?" *<- verificação, if IsInstance*

Se sim → True → entra na festa.
Se não → False → não entra.

```python
if isinstance(pessoa, VIP):
    festa.append(pessoa)
```

**-------------------------------------------------------------------------------------------------------------------------------------**

# Hasattr

*1. O que é:*
Verifica se a instância possui determinado objeto


*2. Como funciona no código:*
```python
if hasattr(item, 'descricao'):
    mensagem_prato = f"{i}. Nome: {item._nome} \n| Preço: {item._preco} \n| Descrição: {item.descricao} \n"
    print(mensagem_prato)
```

Se o item possui o objeto descrição, então imprima mensagem_prato


*3. Uma analogia:*
Por exemplo, você está procurando pessoas que têm carteira de motorista.

A pergunta basicamente é:
"Essa pessoa tem carteira?" *<-pessoa, 'carteira'*

Se tiver → True
Se não tiver → False

```python
if hasattr(pessoa, 'carteira'):
     possui_carteira = 'string'
```

**-------------------------------------------------------------------------------------------------------------------------------------**

# Enumerate()

*1. O que é:*
Função de enumerar uma lista


*2. Como funciona no código:*
```python
for i, item in enumerate(self._cardapio, start=1):
```

para cada indice, enumere os itens da lista cardápio, começando em 1


*3. Uma analogia:*
Funciona bem parecido com uma tabela do excel, ele apenas coloca os numeros do item dentro da lista, precisamos identificar que ele 
comece em 1 pois o contagem do python começa em 0