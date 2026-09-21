# O que é Banco de Dados?

*Banco de Dados* é um sistema utilizado para **armazenar, organizar, consultar e gerenciar informações** de forma estruturada.

Ele permite guardar dados de pessoas, produtos, clientes, pedidos e outras informações necessárias para o funcionamento de um sistema.

Os bancos de dados são utilizados em sites, aplicativos, lojas, empresas e diversos outros sistemas.

*O banco de dados facilita o acesso às informações e permite que elas sejam armazenadas e manipuladas de maneira organizada e segura.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é um SGBD?

*SGBD (Sistema de Gerenciamento de Banco de Dados)* é um software responsável por gerenciar os bancos de dados.

Ele permite criar bancos de dados, armazenar informações, realizar consultas, alterar registros e controlar o acesso aos dados.

Alguns exemplos de SGBDs são:

* MySQL
* PostgreSQL
* SQLite
* Oracle Database
* SQL Server

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é SQL?

*SQL (Structured Query Language)* é uma linguagem utilizada para **interagir com bancos de dados relacionais**.

Com ela, podemos criar tabelas, inserir informações, consultar registros, atualizar dados e excluir informações.

O SQL é utilizado para realizar operações de gerenciamento e manipulação de dados.

*O SQL é uma linguagem de consulta e gerenciamento de dados, não uma linguagem de programação tradicional como Python.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Tabelas?

As *tabelas* são estruturas utilizadas para organizar e armazenar informações dentro de um banco de dados.

Elas são compostas por **linhas e colunas**.

* Colunas: representam os campos ou características dos dados.
* Linhas: representam os registros armazenados.
* Campos: são os espaços destinados a armazenar determinado tipo de informação.
* Registros: são os conjuntos de informações armazenados em uma linha.

As tabelas permitem organizar os dados de forma estruturada e facilitam a consulta e o gerenciamento das informações.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Chaves Primárias e Estrangeiras?

As *chaves* são utilizadas para identificar registros e estabelecer relações entre tabelas.

* PRIMARY KEY: identifica cada registro de forma única dentro de uma tabela.
* FOREIGN KEY: estabelece uma relação entre tabelas por meio de uma chave existente em outra tabela.

*As chaves ajudam a manter a organização e a integridade dos dados.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Tipos de Dados?

Os *tipos de dados* definem quais tipos de informações podem ser armazenados em um campo da tabela.

Alguns tipos comuns são:

**INT:** armazena números inteiros.
**VARCHAR:** armazena textos com tamanho definido.
**TEXT:** armazena textos maiores.
**DATE:** armazena datas.
**DATETIME:** armazena data e horário.
**DECIMAL:** armazena números decimais.
**BOOLEAN:** armazena valores verdadeiro ou falso.

*Cada campo deve utilizar um tipo de dado adequado à informação que será armazenada.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Restrições (Constraints)?

As *restrições* são regras aplicadas aos campos de uma tabela para controlar os dados que podem ser armazenados.

Elas ajudam a manter a consistência e a integridade das informações.

Principais restrições:

**PRIMARY KEY:** define a chave primária.
**FOREIGN KEY:** define a chave estrangeira.
**NOT NULL:** impede que o campo fique vazio.
**UNIQUE:** impede valores duplicados no campo.
**DEFAULT:** define um valor padrão.
**CHECK:** estabelece uma condição para os valores inseridos.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Principais comandos do SQL

Os comandos SQL são utilizados para criar, consultar e manipular informações no banco de dados.

*Comandos de definição da estrutura (DDL):*
**CREATE:** cria bancos de dados, tabelas e outras estruturas.
**ALTER:** altera a estrutura de uma tabela.
**DROP:** exclui uma tabela ou outra estrutura do banco de dados.
**TRUNCATE:** remove todos os registros de uma tabela.

*Comandos de manipulação de dados (DML):*

**INSERT:** insere informações em uma tabela.
**UPDATE:** altera informações existentes.
**DELETE:** exclui registros de uma tabela.
**SELECT:** consulta informações armazenadas.

*Comandos de controle de dados e transações:*

**GRANT:** concede permissões de acesso.
**REVOKE:** remove permissões de acesso.
**COMMIT:** confirma as alterações de uma transação.
**ROLLBACK:** desfaz alterações ainda não confirmadas.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Principais cláusulas do SELECT

As *cláusulas* são utilizadas para definir condições, organizar e filtrar os resultados de uma consulta.

**WHERE:** filtra registros de acordo com uma condição.
**ORDER BY:** organiza os resultados.
**GROUP BY:** agrupa registros com base em um campo.
**HAVING:** filtra grupos de resultados.
**LIMIT:** limita a quantidade de registros retornados.
**DISTINCT:** remove resultados duplicados.
**AS:** define um apelido para uma coluna ou tabela.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Operadores utilizados no SQL

Os *operadores* são utilizados para comparar valores e criar condições nas consultas.

**= :** verifica se dois valores são iguais.
**<> ou !=:** verifica se dois valores são diferentes.
**> :** verifica se um valor é maior que outro.
**< :** verifica se um valor é menor que outro.
**>=:** verifica se um valor é maior ou igual.
**<=:** verifica se um valor é menor ou igual.
**AND:** exige que duas ou mais condições sejam verdadeiras.
**OR:** permite que pelo menos uma condição seja verdadeira.
**NOT:** inverte uma condição.
**LIKE:** pesquisa valores que correspondem a um padrão.
**IN:** verifica se um valor está dentro de uma lista.
**BETWEEN:** verifica se um valor está dentro de um intervalo.
**IS NULL:** verifica se um campo não possui valor.
**IS NOT NULL:** verifica se um campo possui valor.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que são Relacionamentos entre Tabelas?

Os *relacionamentos* são utilizados para conectar tabelas que possuem informações relacionadas.

Eles permitem organizar os dados em diferentes tabelas e estabelecer ligações entre elas.

Principais tipos de relacionamentos:

**Um para um (1:1):** um registro de uma tabela se relaciona com um único registro de outra.
**Um para muitos (1:N):** um registro de uma tabela pode se relacionar com vários registros de outra.
**Muitos para muitos (N:N):** vários registros de uma tabela podem se relacionar com vários registros de outra.

*Os relacionamentos ajudam a evitar a repetição desnecessária de informações e facilitam a organização do banco de dados.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é um Banco de Dados Relacional?

*Banco de Dados Relacional* é um modelo de banco de dados que organiza as informações em tabelas relacionadas entre si.

As tabelas utilizam linhas, colunas e chaves para armazenar e conectar os dados.

Esse modelo permite consultar e manipular informações de diferentes tabelas por meio de relacionamentos.

*O MySQL, PostgreSQL e SQL Server são exemplos de sistemas que trabalham com bancos de dados relacionais.*

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é CRUD?

*CRUD* representa as quatro operações básicas realizadas em um sistema para gerenciar informações de um banco de dados.

**C — Create:** criação de registros.
**R — Read:** leitura ou consulta de registros.
**U — Update:** atualização de registros.
**D — Delete:** exclusão de registros.

Essas operações são utilizadas em sistemas para cadastrar, visualizar, editar e excluir informações.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é uma Consulta (Query)?

*Query* é uma instrução enviada ao banco de dados para realizar uma operação.

Ela pode ser utilizada para consultar, inserir, alterar ou excluir informações, dependendo do comando utilizado.

As consultas permitem que um sistema interaja com o banco de dados e obtenha os dados necessários para seu funcionamento.

**-------------------------------------------------------------------------------------------------------------------------------------**

# O que é Normalização?

*Normalização* é um processo de organização das tabelas e dos dados de um banco de dados.

Seu objetivo é reduzir a repetição desnecessária de informações e evitar problemas durante a inserção, alteração ou exclusão de dados.

A normalização contribui para a organização, consistência e manutenção do banco de dados.

**-------------------------------------------------------------------------------------------------------------------------------------**

# Momento atividade, criação de um banco de dados do 0

* Criar um banco de dados.
* Criar tabelas e definir seus campos.
* Definir os tipos de dados.
* Configurar as chaves primárias e estrangeiras.
* Inserir registros.
* Consultar informações.
* Atualizar registros.
* Excluir registros.
