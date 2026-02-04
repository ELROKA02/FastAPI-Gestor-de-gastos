from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import schemas
import crud
from fastapi.middleware.cors import CORSMiddleware      # Conectar con el frontend


app = FastAPI()

# Configuracion de CORS
origins = [
    "http://127.0.0.1:5500", # Origen del frontend
]
app.add_middleware(
    CORSMiddleware,             # El sistema que gestiona CORS
    allow_origins=origins,   # Origenes permitidos
    allow_credentials=True,   # Permitir credenciales(permite cookies/auth)
    allow_methods=["*"],    # Permitir todos los metodos (GET, POST, etc)
    allow_headers=["*"],    # Permitir todas las cabeceras JSON
)

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

@app.post("/gastos",response_model=schemas.GastoResponse)
def crear_gasto(gasto: schemas.GastoCreate, db: Session = Depends(get_db)):  # FastAPI llama a get_db y le pasa la sesion
    return crud.create_gasto(db=db, gasto=gasto)

@app.get("/gastos", response_model=list[schemas.GastoResponse])
def listar_gastos(db: Session = Depends(get_db)):
    return crud.get_gastos(db=db)

@app.put("/gastos/{gasto_id}", response_model=schemas.GastoResponse)
def actualizar_gasto(gasto_id: int, gasto: schemas.GastoCreate, db: Session = Depends(get_db)):
    gasto_actualizado = crud.update_gasto(db=db, gasto_id=gasto_id, gasto_data=gasto)

    if gasto_actualizado is None:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return gasto_actualizado

@app.delete("/gastos/{gasto_id}", response_model=schemas.GastoResponse)
def eliminar_gasto(gasto_id: int, db: Session = Depends(get_db)):
    gasto = crud.delete_gasto(db=db, gasto_id=gasto_id)

    if gasto is None:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return gasto

@app.get("/gastos/estadisticas")
def obtener_estadisticas(db: Session = Depends(get_db)):
    return {
        "numero_gastos_mes_actual": crud.obtener_total_gastos(db),
        "total_gastos": crud.obtener_gasto_total(db),
        "por_categoria": crud.obtener_total_por_categoria(db),
        "por_mes": crud.obtener_total_por_mes(db)
    }