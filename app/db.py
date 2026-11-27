"""Configuración y dependencias de acceso a la base de datos."""

import os
from collections.abc import Generator

from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

from app.modelos import Actividad, Clase, Intento, Nino, Pregunta  # noqa: F401

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./plataforma.db")
argumentos_conexion = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

motor: Engine = create_engine(DATABASE_URL, connect_args=argumentos_conexion)


def crear_tablas() -> None:
    """Crea las tablas declaradas en los modelos."""
    SQLModel.metadata.create_all(motor)


def obtener_sesion() -> Generator[Session, None, None]:
    """Entrega una sesión y la cierra al terminar la petición."""
    with Session(motor) as sesion:
        yield sesion
