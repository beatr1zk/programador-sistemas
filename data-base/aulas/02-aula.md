# O que é a conexão do Python com o Banco de Dados? *Repositório: data-base-py*

A conexão entre Python e o banco de dados permite que o programa **envie comandos SQL e receba informações do banco**.

- Para realizar a conexão, é utilizada a biblioteca *mysql-connector-python*.
- A conexão contém as informações necessárias para acessar o banco:

*host* → endereço do servidor
*user* → usuário do banco
*password* → senha do banco
*database* → banco de dados que será utilizado

**-------------------------------------------------------------------------------------------------------------------------------------**

# Como preparar o ambiente?

Antes de trabalhar com o banco de dados, é recomendado criar e ativar um **ambiente virtual (venv)** para o projeto.

* Criar o ambiente virtual:
    *python -m venv venv*
  
* Ativar o ambiente virtual:
    *.\venv\Scripts\Activate.ps1*
  
* Caso ocorra um erro de permissão no PowerShell:
    *Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass*
  
* Instalar o conector do MySQL:
    *pip install mysql-connector-python*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é o arquivo db.py?

O arquivo *db.py* é utilizado para concentrar as funções relacionadas ao **banco de dados**.

Nele podem ficar:
  - Função de conexão com o banco
  - Funções para criação das tabelas
  - Funções para inserir informações
  - Funções para consultar informações
  - Funções para alterar informações
  - Funções para excluir informações

**-------------------------------------------------------------------------------------------------------------------------------------**

# Função conectar() *L1 db.py*

A função *conectar()* é responsável por **estabelecer a conexão entre o Python e o MySQL**.

- Utiliza *mysql.connector.connect()*.
- Recebe as informações do banco:
     *host*
     *user*
     *password*
     *database*

- Retorna a conexão criada.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Criação do Banco de Dados

O banco de dados pode ser criado utilizando o **MySQL Workbench**.

- Criar um **Schema** para armazenar as tabelas do projeto.
- O Schema utilizado neste projeto possui o nome:
    *ifood-2*
  
- As tabelas do sistema serão criadas dentro desse Schema.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Tabelas? 

As tabelas são utilizadas para **armazenar e organizar as informações** do sistema.

- Cada tabela possui:
     **Colunas** → definem os tipos de informações armazenadas.
     **Linhas** → representam os registros cadastrados.

- As tabelas podem possuir relacionamentos entre si através de **chaves estrangeiras (FK)**.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Criação de Tabelas pelo Python 

As tabelas podem ser criadas diretamente pelo Python utilizando comandos SQL.

*CREATE TABLE* → cria uma tabela.
*CREATE TABLE IF NOT EXISTS* → cria a tabela somente se ela ainda não existir.
*cursor.execute()* → executa o comando SQL.
*conexao.commit()* → confirma a alteração realizada no banco.
*conexao.close()* → encerra a conexão com o banco.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Tabela restaurantes *L12 db.py*

A tabela *restaurantes* armazena as informações dos restaurantes cadastrados.

- Possui os seguintes campos:
    *id* → identificador único do restaurante.
    *nome* → nome do restaurante.
    *categoria* → categoria do restaurante.
    *ativo* → indica se o restaurante está ativo.
  
- *PRIMARY KEY* → define a chave primária da tabela.
- *AUTO_INCREMENT* → gera automaticamente o próximo ID.
- *NOT NULL* → determina que o campo não pode ficar vazio.
- *DEFAULT FALSE* → define *FALSE* como valor padrão.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Tabela avaliacoes *L27 db.py*

A tabela *avaliacoes* armazena as avaliações realizadas pelos usuários.

- Possui os seguintes campos:
  *id* → identificador da avaliação.
  *nome_usuario* → nome do usuário que realizou a avaliação.
  *nota* → nota atribuída ao restaurante.
  *id_restaurante* → identifica o restaurante avaliado.
  
- A tabela possui uma **chave estrangeira (FK)** relacionada à tabela *restaurantes*.
  
*FOREIGN KEY* → estabelece um relacionamento entre tabelas.
*REFERENCES* → indica qual tabela e campo estão sendo relacionados.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é uma Chave Estrangeira (FK)? *L36 db.py*

A **Foreign Key (FK)** é utilizada para criar um relacionamento entre duas tabelas.

- Ela permite que um registro de uma tabela seja relacionado a um registro de outra.
- No projeto:
    *avaliacoes.id_restaurante*

- está relacionado a *restaurantes.id*.
* Isso permite identificar **qual restaurante recebeu determinada avaliação**.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Inserindo informações no Banco *L43 db.py*

Para adicionar registros em uma tabela, são utilizados comandos SQL de inserção.

*INSERT INTO* → adiciona informações em uma tabela.
*VALUES* → define os valores que serão inseridos.
*%s* → representa os valores que serão enviados pelo Python.
*cursor.execute()* → executa a inserção.
*conexao.commit()* → confirma a inserção no banco.
*conexao.close()* → encerra a conexão.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Função criar_restaurante() 

A função *criar_restaurante()* é responsável por **cadastrar um novo restaurante** no banco de dados.

- Recebe informações como:
    *nome*
    *categoria*
  
- Utiliza *INSERT INTO*.
- Após inserir o registro, utiliza *commit()* para salvar a alteração.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é o app.py?

O arquivo *app.py* pode ser utilizado como o **arquivo principal da aplicação**, chamando as funções criadas no *db.py*.

- As funções podem ser importadas utilizando:
    *from db import ...* → *L1 app.py*
  
- A partir dele é possível:
  * Criar tabelas.
  * Cadastrar informações.
  * Consultar informações.
  * Executar as funcionalidades do sistema.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Consultando informações

Para buscar informações armazenadas no banco de dados, são utilizados comandos de consulta.

*SELECT* → consulta informações.
SELECT * → seleciona todas as colunas.
*FROM* → indica de qual tabela as informações serão buscadas.
*cursor.execute()* → executa a consulta.
*fetchall()* → retorna todos os registros encontrados.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Função listar_restaurantes() *L63 db.py*

A função *listar_restaurantes()* é responsável por **buscar e exibir os restaurantes cadastrados**.

- Utiliza:
*SELECT* → para consultar os dados.
*fetchall()* → para obter os registros.
*for* → para percorrer os restaurantes encontrados.
*print()* → para exibir os registros.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Principais comandos SQL

*CREATE TABLE* → cria uma tabela.
*INSERT INTO* → insere informações.
*SELECT* → consulta informações.
*UPDATE* → altera informações.
*DELETE* → deleta informações.
*WHERE* → define uma condição para o comando.
*PRIMARY KEY* → identifica unicamente cada registro.
*FOREIGN KEY* → cria um relacionamento entre tabelas.
*REFERENCES* → indica a tabela/campo relacionado.
*AUTO_INCREMENT* → gera IDs automaticamente.
*NOT NULL* → impede valores vazios.
*DEFAULT* → define um valor padrão.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Principais funções do mysql.connector

*mysql.connector.connect()* → cria a conexão com o banco.
*conexao.cursor()* → cria um cursor para executar comandos SQL.
*cursor.execute()* → executa um comando SQL.
*cursor.fetchall()* → retorna todos os registros de uma consulta.
*conexao.commit()* → confirma alterações no banco.
*conexao.close()* → encerra a conexão