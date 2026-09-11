from web_scraper import extrair_produtos
from importa_dados import inicializar_dados
from caixa import iniciar_atendimento

def main():
    try:
        print("Iniciando web scraping...")
        extrair_produtos()
        print("Scraping concluído. Carregando dados no banco...")
        inicializar_dados()
        print("Dados importados com sucesso. Iniciando caixa...")
        iniciar_atendimento()
    except Exception as e:
        print(f"Ocorreu um erro na inicialização do sistema: {e}")

if __name__ == "__main__":
    main()