from sqlalchemy import Column, Integer, String, Relationship
from database import Base


class Estudante(Base):
    __tablename__ = 'estudantes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    perfil = Relationship('Perfil', back_populates='estudante', uselist=False, cascade='all, delete-orphan')


class Perfil(Base):
    __tablename__ = 'perfis'

    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    estudante_id = Column('Integer', ForeignKey('estudantes.id'), unique=True)
    estudante = Relationship('Estudante', back_populates='perfil')