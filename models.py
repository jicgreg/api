from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), unique=True, nullable=False)
    domicilio = Column(String(80), unique=True, nullable=False)
    telefono = Column(Integer, unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

class Prestamo(Base):
    __tablename__ = 'prestamos'
    id_prestamo = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, unique=True, nullable=False)
    total_libros = Column(Integer, unique=True, nullable=False)
    fecha_devolucion = Column(DateTime(timezone=True), unique=True, nullable=False)

class Libro(Base):
    __tablename__ = 'libros'
    id_libro = Column(Integer, primary_key=True)
    titulo = Column(String(80), unique=True, nullable=False)
    autor = Column(String(80), unique=True, nullable=False)
    editorial = Column(String(80), unique=True, nullable=False)
    genero = Column(String(120), unique=True, nullable=False)
    total_paginas = Column(Integer, unique=True, nullable=False)
    isbn = Column(String(50), unique=True, nullable=False)

