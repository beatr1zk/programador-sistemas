**INFORMAÇÕES**

**O que vamos aprender?**
- Instalar o Django via pip e gerenciar dependências
- Django e a arquitetura MVT (Model, View, Template)
- Criar e ativar um ambiente virtual (venv)
- Criar um projeto Django
- Subir o servidor de desenvolvimento
- Organizar pastas de uma forma profissional
  

**Porque o Djando é uma ferramenta interessante?**
*É gratuito e tem algumas funções que ajudam muito no desenvolvimento:*

- Operações CRUD e ORM nativo - sem precisar conectar o SQL manualmente
- Tem interface de administrador pronta para uso imediato
- Arquitetura MVT (Model, View, Template)
- Proteções contra XSS e SQL Injection

*--------------------------------------------------------------------------------------------------------------------------*

**INSTALAÇÃO**

**Como instalar o ambiente virtual?**
1º - python -m pip install virtualenv 
2º - python -m virtualenv --version (*verificar instalação*)
3º - python -m venv venv (*apenas se der erro: passo 4º*)
4º - Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass 
5º - venv .\venv\Scripts\Activate.ps1

Para parar de executar: deactivate


**Como instalar Django?**
1º - pip install django
2º - pip freeze (*lista o que está instalado no ambiente virtual*)
3º - pip freeze > requirements.txt (*cria um arquivo chamado requirements.txt contendo todas as bibliotecas instaladas no AV*)

*--------------------------------------------------------------------------------------------------------------------------*

**COMANDOS**

**Comandos do django**
Para listar os comandos do django utilize: *django-admin help*, os mais utilizados são:

- makemigrations (cria arquivos de migração com base nas alterações feitas nos modelos.)
- migrate (aplica as migrações ao banco de dados, criando ou alterando tabelas.)
- startapp (cria uma nova aplicação dentro de um projeto Django.)
- startproject (cria um novo projeto Django com sua estrutura inicial de arquivos.)

**Como utilizar o Django?**
1º - django-admin startproject setup . (*cria o setup do django*)
2º - python manage.py runserver (*inicializa o server e disponibiliza a URL*)

*--------------------------------------------------------------------------------------------------------------------------*