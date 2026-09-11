import sqlite3

conexao = sqlite3.connect("Dados/mercado.db")
with open("Dados/cria_banco.sql", "r", encoding="utf-8") as f:
    conexao.executescript(f.read())
conexao.close()
print("Banco criado com sucesso!")