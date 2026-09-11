import requests
from bs4 import BeautifulSoup
import csv
import os
from constantes import URL_PRODUTOS, ARQUIVO_PRODUTOS_CSV

def extrair_produtos():
    resposta = requests.get(URL_PRODUTOS)
    resposta.raise_for_status()
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    produtos = []
    itens = soup.find_all('div', class_='produto')
    for item in itens:
        nome = item.find('h2').text.strip()
        preco_texto = item.find('p', class_='preco').text.strip().replace('R$', '').replace(',', '.')
        preco = float(preco_texto)
        produtos.append({'nome': nome, 'preco': preco})
        
    os.makedirs("Dados", exist_ok=True)
    with open(ARQUIVO_PRODUTOS_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['nome', 'preco'])
        writer.writeheader()
        writer.writerows(produtos)