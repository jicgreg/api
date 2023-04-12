import  requests, jsonify, make_response

import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import User as SchemaUser
from schema import Prestamo as SchemaPrestamo
from schema import Libro as SchemaLibro

from schema import User
from schema import Prestamo
from schema import Libro

from models import User as ModelUser
from models import Prestamo as ModelPrestamo
from models import Libro as ModelLibro
import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"mensaje": "Bienvenido. Es un placer atenderle"}

 # create a user
@app.post('/users/', response_model=SchemaUser)
async def user(user: SchemaUser):
  try:
    data = requests.get_json()
    new_user = User(nombre=data['nombre'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'usuario creado'}), 201)
  except :
    return make_response(jsonify({'message': 'error creando usuario'}), 500)
  
# create a prestamo
@app.post('/prestamos/',response_model=SchemaPrestamo)
async def prestamo(prestamo: SchemaPrestamo):
  try:
    data = requests.get_json()
    new_prestamo = Prestamo(id_prestamo=data['id_prestamo'], id_usuario=data['id_usuario'],total_libros=data['total_libros'],fecha_devolucion=data['fecha_devolucion'])
    db.session.add(new_prestamo)
    db.session.commit()
    return make_response(jsonify({'message': 'prestamo creado'}), 201)
  except :
    return make_response(jsonify({'message': 'error creando prestamo'}), 500)  

# create a libro
@app.post('/libros/', response_model=SchemaLibro)
async def libro(libro: SchemaLibro):
  try:
    data = requests.get_json()
    new_libro = Libro(id_libro=data['id_libro'], titulo=data['titulo'],autor=data['autor'],editorial=data['editorial'],genero=data['genero'],total_paginas=data['total_paginas'],isbn=data['isbn'])
    db.session.add(new_libro)
    db.session.commit()
    return make_response(jsonify({'message': 'libro creado'}), 201)
  except :
    return make_response(jsonify({'message': 'error creando libro'}), 500)  


# get all users
@app.route('/users/', methods=['GET'])
def get_users():
  try:
    users = db.session.query(ModelUser).all()
    return make_response(jsonify([user.json() for user in users]), 200)
  except :
    return make_response(jsonify({'message': 'error getting users'}), 500)

# get all prestamos
@app.route('/prestamos/', methods=['GET'])
def get_prestamos():
  try:
    prestamo = db.session.query(ModelPrestamo).all()
    return make_response(jsonify([prestamo.json() for prestamo in prestamo]), 200)
  except :
    return make_response(jsonify({'message': 'error getting prestamos'}), 500)

# get all libros
@app.route('/libros/', methods=['GET'])
def get_libros():
  try:
    libro = db.session.query(ModelLibro).all()
    return make_response(jsonify([libro.json() for libro in libro]), 200)
  except :
    return make_response(jsonify({'message': 'error getting prestamos'}), 500)


# get a user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error getting user'}), 500)
  
  # get a prestamos by id  
@app.route('/prestamos/<int:id>', methods=['GET'])
def get_prestamo(id):
  try:
    prestamo = Prestamo.query.filter_by(id=id).first()
    if prestamo:
      return make_response(jsonify({'prestamo': prestamo.json()}), 200)
    return make_response(jsonify({'message': 'prestamo not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error getting prestamo'}), 500)
  
# get a libros by id
@app.route('/libros/<int:id>', methods=['GET'])
def get_libro(id):
  try:
    libro = Libro.query.filter_by(id=id).first()
    if libro:
      return make_response(jsonify({'libro': libro.json()}), 200)
    return make_response(jsonify({'message': 'libro not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error getting libro'}), 500)

# update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = requests.get_json()
      user.nombre = data['nombre']
      user.email = data['email']
      db.session.commit()
      return make_response(jsonify({'message': 'user updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error updating user'}), 500)
  
# update a prestamo
@app.route('/prestamos/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    prestamo = Prestamo.query.filter_by(id=id).first()
    if prestamo:
      data = requests.get_json()
      prestamo.id_usuario= data['id_usuario']
      prestamo.total_libros = data['total_libro']
      prestamo.fecha_devolucion = data['fecha_devolucion ']
      
      db.session.commit()
      return make_response(jsonify({'message': 'prestamo updated'}), 200)
    return make_response(jsonify({'message': 'prestamo not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error updating prestamo'}), 500)

# update a libro
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = requests.get_json()
      user.id_libro = data['id_libro']
      user.titulo  = data['titulo ']
      user.autor = data['autor']
      user.editorial  = data['editorial ']
      user.genero = data['genero']
      user.total_paginas = data['total_paginas']
      user.isbn  = data['isbn ']

      db.session.commit()
      return make_response(jsonify({'message': 'libro updated'}), 200)
    return make_response(jsonify({'message': 'libro not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error updating libro'}), 500)

# delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      db.session.delete(user)
      db.session.commit()
      return make_response(jsonify({'message': 'user deleted'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error deleting user'}), 500)
	
  # delete prestamo
@app.route('/prestamos/<int:id>', methods=['DELETE'])
def delete_prestamo(id):
  try:
    prestamo = Prestamo.query.filter_by(id=id).first()
    if prestamo:
      db.session.delete(prestamo)
      db.session.commit()
      return make_response(jsonify({'message': 'prestamo deleted'}), 200)
    return make_response(jsonify({'message': 'prestamo not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error deleting prestamo'}), 500)
	
  # delete libro
@app.route('/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
  try:
    libro= Libro.query.filter_by(id=id).first()
    if libro:
      db.session.delete(libro)
      db.session.commit()
      return make_response(jsonify({'message': 'libro deleted'}), 200)
    return make_response(jsonify({'message': 'libro not found'}), 404)
  except :
    return make_response(jsonify({'message': 'error deleting libro'}), 500) 


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)