from sqlalchemy.orm import Session
from models import Cliente

def buscar_por_id(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def criar(db: Session, cliente: Cliente):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente