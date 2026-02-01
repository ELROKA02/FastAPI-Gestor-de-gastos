from datetime import date
from pydantic import BaseModel

class GastoBase(BaseModel):
    descripcion: str
    categoria: str
    monto: float
    fecha: date

class GastoCreate(GastoBase):
    pass

class GastoResponse(GastoBase):
    id: int

    class Config:
        from_attributes = True