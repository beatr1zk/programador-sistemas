criei um repositorio novo para fazer a atividade, se chama da-base-py

ativar o venv
python -m venv venv
.\venv\Scripts\Activate.ps1
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass *se der erro*
pip install mysql-connector-python

criacao da pasta db.py para conectar o banco:
```python
import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host= "",
        user= "",
        password= "",
        database= ""
)
    return conexao
```

no SQL workbanch crie:
Schema com nome de ifood-2

para criação de tabelas, ainda em db.py:
```python
def tabela_restaurante():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_restaurantes = """
        CREATE TABLE IF NOT EXISTS restaurantes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            ativo BOOlEAN DEFAULT FALSE NOT NULL
        )
    """
    cursor.execute(criar_tabela_restaurantes)
    conexao.commit()
    conexao.close()
```

para criar itens dentro de uma tabela:
```python
def criar_restaurante(nome, categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO restaurantes(nome, categoria)
        VALUES (%s, %s)
    """, (nome, categoria))
    conexao.commit()
    conexao.close()
```

em app.py para preencher as informacoes:
```python
from db import tabela_restaurante, criar_restaurante

tabela_restaurante()

criar_restaurante("La Mafia", "Italiana")
```