# build a schema using pydantic
from pydantic import BaseModel

class User(BaseModel):
    
    id:int
    nombre :str
    domicilio :str
    telefono :int
    email :str
    
    class Config:
        orm_mode = True

class Prestamo(BaseModel):
    id_prestamo :int
    id_usuario :int
    total_libros :int
    fecha_devolucion:str

    class Config:
        orm_mode = True

class Libro(BaseModel):
    id_libro :int
    titulo :str
    autor :str
    editorial :str
    genero :str
    total_paginas :int
    isbn :str

    class Config:
        orm_mode = True
