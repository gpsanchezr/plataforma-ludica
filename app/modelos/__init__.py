"""Modelos de datos de la plataforma."""

from datetime import datetime

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class Clase(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    codigo: str = Field(min_length=6, max_length=6, unique=True, index=True)


class Nino(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    alias: str
    avatar: str
    clase_id: int = Field(foreign_key="clase.id")


class Actividad(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str = ""
    orden: int


class Pregunta(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    enunciado: str
    opciones: list[str] = Field(sa_column=Column(JSON, nullable=False))
    respuesta_correcta: str
    actividad_id: int = Field(foreign_key="actividad.id")


class Intento(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nino_id: int = Field(foreign_key="nino.id")
    actividad_id: int = Field(foreign_key="actividad.id")
    aciertos: int
    total: int
    duracion_segundos: int
    fecha: datetime
