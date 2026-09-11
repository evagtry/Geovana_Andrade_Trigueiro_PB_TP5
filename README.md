# Sistema de Caixa - Projeto TP5

## Descrição do Projeto
Este é um projeto acadêmico de Engenharia de Software desenvolvido para o Instituto Infnet. O sistema simula o funcionamento de um terminal de caixa de mercado, focado na integração de múltiplas tecnologias de manipulação de dados e arquitetura de software.

O projeto realiza a coleta de dados de produtos via web scraping, importa dados de clientes pré-existentes, e estrutura todas as informações em um banco de dados relacional. A aplicação foi construída seguindo uma arquitetura em camadas (Repository, Service e CRUD) para garantir a separação de responsabilidades e a manutenibilidade do código.

## Tecnologias Utilizadas
* **Python 3:** Linguagem principal do projeto.
* **SQLAlchemy:** Mapeamento Objeto-Relacional (ORM) para interação com o banco de dados.
* **Pandas:** Processamento e importação em massa de dados (CSV e JSON) para o banco.
* **BeautifulSoup4 & Requests:** Web scraping para extração automatizada da lista de produtos.
* **SQLite:** Banco de dados relacional leve para persistência das informações locais.

## Estrutura do Projeto
* `main.py`: Arquivo principal que orquestra a extração, carregamento e o fluxo de caixa.
* `web_scraper.py`: Responsável por raspar os dados da página web e gerar o arquivo CSV.
* `importa_dados.py`: Utiliza Pandas para transferir os dados do CSV e do JSON para o banco de dados.
* `database.py` e `models.py`: Configuração de conexão do SQLAlchemy e definição das tabelas.
* `executa_sql.py`: Script de inicialização e criação da estrutura do banco de dados SQLite.
* `repository/`, `service/`, `crud/`: Diretórios que compõem a arquitetura em camadas para regras de negócio e acesso a dados (focado na entidade Cliente).
* `Dados/`: Diretório gerado automaticamente que armazena os arquivos estáticos e o banco de dados (`mercado.db`).

## Como Executar

1. **Instale as dependências necessárias:**
   No terminal, execute o comando:
   ```bash
   python -m pip install requests beautifulsoup4 pandas sqlalchemy
