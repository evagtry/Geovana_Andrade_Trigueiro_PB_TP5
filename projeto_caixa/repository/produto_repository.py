from sqlalchemy.orm import Session
from models import Produto

def buscar_por_id(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def listar_todos(db: Session):
    return db.query(Produto).all()

def criar(db: Session, produto: Produto):
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto