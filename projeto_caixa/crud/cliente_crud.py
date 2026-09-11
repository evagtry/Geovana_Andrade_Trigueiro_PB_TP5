from sqlalchemy.orm import Session
from service import cliente_service

def verificar_ou_cadastrar_cliente(db: Session):
    try:
        cliente_id = int(input("Informe o ID do cliente: "))
        cliente = cliente_service.obter_cliente(db, cliente_id)
        
        if cliente:
            print(f"Bem-vindo(a) de volta, {cliente.nome}!")
            return cliente
            
        print("Cliente não encontrado. Iniciando cadastro...")
        nome = input("Informe o nome do novo cliente (max 50 carac.): ")
        if not nome or len(nome) > 50:
            raise ValueError
            
        novo_cliente = cliente_service.registrar_cliente(db, nome)
        print(f"Cliente {novo_cliente.nome} cadastrado com sucesso!")
        return novo_cliente
        
    except ValueError:
        print("Dados inválidos fornecidos.")
        return None