from sqlalchemy.orm import Session
from service import produto_service

def consultar_produto_por_id(db: Session):
    try:
        produto_id = int(input("Informe o ID do produto: "))
        produto = produto_service.obter_produto(db, produto_id)
        if produto:
            print(f"Produto: {produto.nome} | Preço: R$ {produto.preco:.2f}")
            return produto
        print("Produto não encontrado.")
        return None
    except ValueError:
        print("ID inválido.")
        return None

def listar_todos_produtos(db: Session):
    produtos = produto_service.listar_produtos(db)
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(f"[{p.id}] {p.nome} - R$ {p.preco:.2f}")