from sqlalchemy.orm import Session
from repository import cliente_repository
from models import Cliente

def obter_cliente(db: Session, cliente_id: int):
    return cliente_repository.buscar_por_id(db, cliente_id)

def registrar_cliente(db: Session, nome: str):
    novo_cliente = Cliente(nome=nome)
    return cliente_repository.criar(db, novo_cliente)