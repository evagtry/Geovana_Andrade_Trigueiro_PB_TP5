from database import SessionLocal
from crud.cliente_crud import verificar_ou_cadastrar_cliente

def iniciar_atendimento():
    db = SessionLocal()
    try:
        cliente = verificar_ou_cadastrar_cliente(db)
        if cliente:
            print("Atendimento liberado. Iniciando caixa...")
        else:
            print("Atendimento cancelado devido a erro de identificação.")
    finally:
        db.close()