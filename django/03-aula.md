# INFORMAÇÕES
Criei um repositório separado para executar os comandos, o nome é: projeto-stoque está no GIT

# O que vamos aprender?
- Configurar a pasta de templates no settings.py
- Usar a função render para renderizar arquivos HTML
- Organizar templates por app (templates/galeria)

**----------------------------------------------------------------------------------------------------**

# Sequência lógica de configuração
- Abrir setup > settings.py e localizar a seção **TEMPLATES*
- Configurar 'DIRS': [os.path.join(BASE_DIR,='templates')] → Informa ao Django onde procurar os 
arquivos HTML do projeto
- Criar a pasta templates na *raiz* do projeto (ex: dentro de stoque)
- Criar uma pasta exclusiva do seu app
- Criar o arquivo index.html dentro dessa pasta, com um <h1> e um <p>
- Em produtos > views.py, importar e usar a *função render* no lugar do HttpResponse:
    from django.shortcuts import render

    def index(request):
        return render(request, 'produtos/index.html') -> dando o caminho da pasta

**----------------------------------------------------------------------------------------------------**

# Carregando CSS e imagens no Django
- O Django precisa ser configurado para saber onde procurar e onde reunir esses arquivos.

## Duas configurações principais no settings.py:
- STATICFILES_DIRS → onde o Django procura os arquivos estáticos durante o desenvolvimento (ex: setup/static)
- STATIC_ROOT → para onde o Django coleta todos os arquivos estáticos (usado em produção)

# Sequência lógica de configuração
- Criar a *pasta /static* dentro de /setup
- Mover os arquivos CSS e outros ativos visuais para essa pasta
- Configurar *STATICFILES_DIRS* e *STATIC_ROOT* no settings.py:
    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]

    STATIC_ROOT = BASE_DIR / 'staticfiles'

- Rodar python manage.py collectstatic → Reúne todos os arquivos estáticos configurados nos diretórios definidos
- No index.html, adicionar *{% load static %}* no topo do arquivo 
- Trocar os caminhos fixos de CSS/imagens pela tag *{% static caminho/do/arquivo.css'%}*