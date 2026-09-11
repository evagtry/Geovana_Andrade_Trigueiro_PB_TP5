import pandas as pd
from sqlalchemy import text
from database import engine
from constantes import ARQUIVO_PRODUTOS_CSV, ARQUIVO_CLIENTES_JSON
import os

def carregar_produtos():
    if os.path.exists(ARQUIVO_PRODUTOS_CSV):
        df_produtos = pd.read_csv(ARQUIVO_PRODUTOS_CSV)
        with engine.connect() as con:
            con.execute(text("DELETE FROM produtos"))
            con.commit()
        df_produtos.to_sql('produtos', con=engine, if_exists='append', index=False)

def carregar_clientes():
    if os.path.exists(ARQUIVO_CLIENTES_JSON):
        df_clientes = pd.read_json(ARQUIVO_CLIENTES_JSON)
        clientes_existentes = pd.read_sql('clientes', con=engine)
        novos_clientes = df_clientes[~df_clientes['id'].isin(clientes_existentes['id'])]
        
        if not novos_clientes.empty:
            novos_clientes.to_sql('clientes', con=engine, if_exists='append', index=False)

def inicializar_dados():
    carregar_produtos()
    carregar_clientes()