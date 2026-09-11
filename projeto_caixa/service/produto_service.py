from sqlalchemy.orm import Session
from repository import produto_repository
from models import Produto

def obter_produto(db: Session, produto_id: int):
    return produto_repository.buscar_por_id(db, produto_id)

def listar_produtos(db: Session):
    return produto_repository.listar_todos(db)

def registrar_produto(db: Session, nome: str, preco: float):
    novo_produto = Produto(nome=nome, preco=preco)
    return produto_repository.criar(db, novo_produto)