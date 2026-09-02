**INFORMAÇÕES**
Criei um repositório separado para executar os comandos, o nome é: projeto-stoque

**O que vamos aprender?**
- SECURITY_KEY
- Usar variáveis de ambiente com python-dotenv
- Configurar idioma e fuso horário do projeto
- Organizar rotas (urls.py) de forma profissional, isolando cada app

**Sequencia de comandos:**
- python -m venv venv
- .\venv\Scripts\Activate.ps1  
- Set-ExecutionPolicy RemoteSigned -Scope CurrentUser (*Caso der erro no 1º*)
- pip install python-dotenv
- pip freeze > requirements.txt
  
- crie um arquivo com o nome: *.env* na raiz do projeto
- Procure dentro da *pasta setup > settings.py* a linha com a SECRET_KEY e a copie
- Cole a chave completa dentro do arquivo *.env* 
- Volte para o settings.py e substitua a informação da SECRET_KEY após o '=' por: *str(os.getenv('SECRET_KEY'))*
- No mesmo arquivo arrume as importações que devem ficar assim:
    import os
    from pathlib import Path
    from dotenv import load_dotenv
    load_dotenv()

- Ainda dentro da pasta settings vamos alterar a linguagem e hora
- Scrolle para baixo e mude a informação da linguagem em: *LANGUAGE_CODE = 'en-us'* para *'pt-br'*
- Altere tambem a informação de *TIME_ZONE = 'UTC'* para *'America/Sao_Paulo'*

- python manage.py startapp produtos
- dentro de *setup > settings* adicione na lista de *INSTALLED_APPS* o nome da pasta criada, nesse caso: *'produtos',*
- adicione também mais uma informação com nome *'galeria',*

- django-admin startproject setup .
- python manage.py runserver