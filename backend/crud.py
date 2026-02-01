from sqlalchemy.orm import Session
import models
import schemas


def create_gasto(db: Session, gasto: schemas.GastoCreate):
    nuevo_gasto = models.Gasto(
        descripcion=gasto.descripcion,
        categoria=gasto.categoria,
        monto=gasto.monto,
        fecha=gasto.fecha,
    )

    db.add(nuevo_gasto)         # Marcamos para guardar
    db.commit()                 # Confirmamos los cambios
    db.refresh(nuevo_gasto)     # Refresca el objeto con los datos de la BD (ej. id generado)

    return nuevo_gasto

def get_gastos(db: Session):
    return db.query(models.Gasto).all()

def update_gasto(db: Session, gasto_id: int, gasto_data: schemas.GastoCreate):
    gasto = db.query(models.Gasto).filter(models.Gasto.id == gasto_id).first()

    if not gasto:
        return None
    
    gasto.descripcion = gasto_data.descripcion
    gasto.categoria = gasto_data.categoria
    gasto.monto = gasto_data.monto
    gasto.fecha = gasto_data.fecha

    db.commit()
    db.refresh(gasto)
    return gasto

def delete_gasto(db: Session, gasto_id: int):
    gasto = db.query(models.Gasto).filter(models.Gasto.id == gasto_id).first()

    if not gasto:
        return None
    
    db.delete(gasto)
    db.commit()

    return gasto