# O que é Flask?

Flask é um *framework web escrito em Python* utilizado para criar aplicações e sistemas que funcionam através da internet.
Ele facilita a criação de sites, APIs e sistemas web, fornecendo recursos para trabalhar com **rotas, requisições, páginas HTML e templates**.
É considerado um framework leve e flexível, pois permite que o desenvolvedor escolha quais recursos deseja utilizar.

*O Flask funciona como uma ponte entre o código Python e as páginas que o usuário acessa pelo navegador.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# Instalação do Flask

Para utilizar o Flask em um projeto Python, primeiro é necessário instalá-lo no ambiente virtual do projeto.

A instalação pode ser realizada através do *pip*:
```bash
pip install flask
```

O *pip* é o gerenciador de pacotes do Python. Ele permite instalar bibliotecas e frameworks que não fazem parte da instalação padrão do Python.


Depois da instalação, podemos importar o Flask no nosso código:
```python
from flask import Flask
```

Em seguida, podemos criar uma aplicação Flask:
```python
from flask import Flask

app = Flask(__name__)
```

O Flask(__name__) cria uma *aplicação Flask*.

*A variável `app` representa a nossa aplicação e será utilizada para configurar as rotas e executar o sistema.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Rotas?

*Rotas* são os *endereços que determinam quais partes da aplicação podem ser acessadas* através de uma URL.

No Flask, uma rota é criada utilizando o `@app.route()`:
```python
@app.route('/')
def inicio():
    return 'Olá, mundo!'
```

Nesse exemplo, a rota `/` representa a *página inicial* da aplicação.

Quando o usuário acessa:

```text
http://localhost:5000/
```

o Flask identifica a rota `/` e executa a função `inicio()`.

*O Flask decide qual função deve ser executada com base na URL acessada e no método HTTP utilizado.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Templates?

*Templates* são arquivos utilizados para criar a *interface HTML da aplicação*.

Normalmente, os templates ficam dentro de uma pasta chamada: templates/


Por exemplo:
projeto/
│
├── app.py
│
└── templates/
    └── cadastro.html

Para utilizar um template no Flask, podemos importar o `render_template`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('cadastro.html')
```

Nesse caso, o Flask procura o arquivo `cadastro.html` dentro da pasta `templates` e envia essa página para o navegador.

*O `render_template()` é utilizado para renderizar e exibir arquivos HTML dentro da aplicação Flask.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é uma Requisição?

*Requisição HTTP* é uma comunicação feita pelo navegador ou por outro programa para solicitar que o servidor execute alguma ação.
Por exemplo, quando acessamos uma página pela internet, o navegador envia uma requisição para o servidor.

Existem diferentes métodos HTTP, mas os principais utilizados em um CRUD são:
* *GET* → buscar ou visualizar informações
* *POST* → enviar ou cadastrar informações
* *PUT* → atualizar informações
* *DELETE* → excluir informações

*Esses métodos ajudam o servidor a entender qual ação deve ser realizada sobre determinado recurso.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# Requisição GET

GET é utilizado principalmente para *buscar ou visualizar informações*.

Por exemplo:
```python
@app.route('/clientes', methods=['GET'])
def clientes():
    return 'Lista de clientes'
```

Quando o usuário acessa `/clientes`, o navegador realiza uma requisição GET e o Flask executa a função `clientes()`.

- Um exemplo comum seria utilizar GET para:
* visualizar uma lista de produtos
* consultar clientes
* abrir uma página
* visualizar informações cadastradas

*GET normalmente é utilizado quando queremos receber ou consultar dados do servidor.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# Requisição POST

*POST* é utilizado para *enviar dados para o servidor*.

Um exemplo comum é o preenchimento de um formulário de cadastro.

```python
@app.route('/cadastro', methods=['POST'])
def cadastro():
    return 'Cadastro realizado!'
```

Quando o usuário envia o formulário, os dados são enviados através de uma requisição POST para a rota `/cadastro`.

Por exemplo, um formulário HTML poderia enviar:
Nome: Beatriz
Email: beatriz@email.com

O Flask recebe essas informações e pode posteriormente armazená-las no banco de dados.

*POST é utilizado principalmente quando precisamos enviar novos dados para serem processados ou armazenados.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# GET e POST na mesma rota

É possível permitir que uma mesma rota aceite diferentes métodos HTTP.

Um exemplo muito comum é:

```python
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # realizar cadastro
        pass

    return render_template('cadastro.html')
```

Nesse caso, a mesma rota `/cadastro` pode realizar duas funções diferentes.

- Quando utilizamos *GET*, a página de cadastro pode ser exibida: *GET → /cadastro → exibe o formulário*
- Quando utilizamos *POST*, os dados preenchidos no formulário podem ser enviados: *POST → /cadastro → processa os dados*

Para verificar qual método foi utilizado, podemos utilizar: **request.method**

Por isso, também precisamos importar `request`:
```python
from flask import Flask, render_template, request
```

*Dessa forma, uma única rota pode exibir o formulário através do GET e processar os dados através do POST.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# Como o Flask decide qual View chamar?

O Flask utiliza a *URL e o método HTTP* da requisição para determinar qual função deverá ser executada.

Por exemplo:
```python
@app.route('/cadastro', methods=['GET'])
def cadastro():
    return 'Formulário de cadastro'
```

Quando ocorre: GET /cadastro


o Flask chama a função `cadastro()`.

Se tivermos:
```python
@app.route('/clientes', methods=['GET'])
def clientes():
    return 'Lista de clientes'
```

Quando ocorre: GET /clientes

o Flask chama a função `clientes()`.

*Portanto, podemos pensar que o Flask funciona como um roteador: ele recebe uma requisição, verifica a URL e o método HTTP e direciona a requisição para a função correspondente.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é uma View?

*View* é a *função responsável por responder a uma determinada requisição*.

Por exemplo:
```python
@app.route('/clientes')
def clientes():
    return 'Lista de clientes'
```

Nesse exemplo:
* `/clientes` → é a **rota**
* `clientes()` → é a **view**
* `'Lista de clientes'` → é a **resposta**

Quando alguém acessa `/clientes`, o Flask identifica a rota e executa a view correspondente.

*A view contém a lógica que será executada quando determinada rota for acessada.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é CRUD?

*CRUD* é uma sigla formada pelas quatro operações básicas realizadas em sistemas que trabalham com dados:

* C → Create → Criar
* R → Read → Ler
* U → Update → Atualizar
* D → Delete → Excluir

Essas quatro operações são utilizadas para *criar, consultar, modificar e excluir dados*.

Por exemplo, em um sistema de clientes:
* Create → cadastrar um novo cliente
* Read → visualizar os clientes cadastrados
* Update → alterar os dados de um cliente
* Delete → excluir um cliente

*CRUD representa o ciclo básico de manipulação dos dados em uma aplicação.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# C → Create → POST

**Create** significa *criar um novo registro*.

No CRUD, normalmente utilizamos o método *POST* para realizar essa operação.

Exemplo:
```python
@app.route('/clientes', methods=['POST'])
def criar_cliente():
    # cadastrar cliente
    pass
```

Nesse caso, o servidor recebe os dados enviados pelo usuário e pode inseri-los no banco de dados.

POST /clientes

Nome: Beatriz
Email: beatriz@email.com


O sistema recebe esses dados e cria um novo registro.

*CREATE é utilizado quando queremos adicionar novos dados ao sistema.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# R → Read → GET

**Read** significa *ler ou consultar informações*.

No CRUD, normalmente utilizamos o método **GET**.

Exemplo:
```python
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    # buscar clientes no banco
    pass
```

Nesse caso, a aplicação consulta os dados existentes e pode apresentá-los ao usuário.

Por exemplo: GET /clientes


Pode retornar:
1 - Beatriz
2 - João
3 - Maria

*READ é utilizado quando queremos consultar ou visualizar dados que já existem.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# U → Update → PUT

**Update** significa *atualizar ou alterar um registro existente*.

No CRUD, o método HTTP normalmente associado a essa operação é o **PUT**.

Exemplo:
```python
@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    # atualizar cliente
    pass
```

Nesse exemplo: PUT /clientes/1


poderia significar que queremos alterar o cliente que possui o ID `1`.

Por exemplo:
Nome antigo: Beatriz
Nome novo: Beatriz Kava

O sistema localiza o registro e modifica suas informações.

*UPDATE é utilizado quando queremos alterar dados que já estão cadastrados.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# D → Delete → DELETE

**Delete** significa *excluir um registro*.

No CRUD, utilizamos o método HTTP **DELETE**.

Exemplo:
```python
@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    # excluir cliente
    pass
```

Nesse caso: DELETE /clientes/1

indica que o sistema deve excluir o cliente que possui o ID `1`.

*DELETE é utilizado quando queremos remover um registro existente do sistema.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# CRUD e os métodos HTTP

Podemos relacionar as operações do CRUD com os principais métodos HTTP:

- *C* → Create → POST → criar
- *R* → Read → GET → consultar
- *U* → Update → PUT → atualizar
- *D* → Delete → DELETE → excluir

Um exemplo de sistema de clientes seria:
POST   /clientes       → criar cliente
GET    /clientes       → listar clientes
PUT    /clientes/1     → atualizar cliente 1
DELETE /clientes/1     → excluir cliente 1

**Dessa forma, o CRUD organiza as principais operações de manipulação de dados, enquanto os métodos HTTP indicam ao servidor qual operação está sendo solicitada.**