from sqlalchemy.orm import Session
from models import Gasto
import schemas
from sqlalchemy import func, extract     # Funciones SQL como SUM, COUNT, etc.
from datetime import date


def create_gasto(db: Session, gasto: schemas.GastoCreate):
    nuevo_gasto = Gasto(
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
    return db.query(Gasto).all()

def update_gasto(db: Session, gasto_id: int, gasto_data: schemas.GastoCreate):
    gasto = db.query(Gasto).filter(Gasto.id == gasto_id).first()

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
    gasto = db.query(Gasto).filter(Gasto.id == gasto_id).first()

    if not gasto:
        return None
    
    db.delete(gasto)
    db.commit()

    return gasto

################### Estadísticas ###################
def obtener_gasto_total(db: Session):
    gastos = db.query(Gasto).all()
    total = 0
    for gasto in gastos:
        total += float(gasto.monto)
    
    return total

def obtener_total_por_categoria(db: Session):
    resultados = (
        db.query(
            Gasto.categoria,
            func.sum(Gasto.monto).label("Total")
        )
        .group_by(Gasto.categoria)
        .all()
    )

    return [
        {"categoria": categoria, "total": float(total)}
        for categoria, total in resultados
    ]

def obtener_total_por_mes(db: Session):
    resultados = (
        db.query(
            func.date_format(Gasto.fecha, "%Y-%m").label("mes"),
            func.sum(Gasto.monto).label("Total")
        )
        .group_by("mes")
        .order_by("mes")
        .all()
    )

    return [
        {"mes": mes, "total": float(total)}
        for mes, total in resultados
    ]

def obtener_total_gastos(db: Session):
    # Retorna el total de gastos registrados
    hoy = date.today()

    return (
        db.query(func.count(Gasto.id))
        .filter(
            extract("year", Gasto.fecha) == hoy.year,
            extract("month", Gasto.fecha) == hoy.month
        )
        .scalar()   # Retorna un unico valor (no una tupla
    )

