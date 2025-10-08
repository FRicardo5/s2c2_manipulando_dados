from typing import Optional, List
from pydantic import BaseModel

class EstudanteBase(BaseModel):
    id: int
    nome: str
    idade: int
    perfil: Optional['Perfil'] = None

    class Config:
        from_attributes = True

class EstudanteCreate(BaseModel):
    nome: str
    idade: int  
    perfil: PerfilCreate

class PerfilBase(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str 