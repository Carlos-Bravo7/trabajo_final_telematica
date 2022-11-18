import flask
import os
from flask import request

app1 = flask.Flask(__name__)

@app1.route('/')
def inicio():
	return "pagina de inicio d ela red social"

@app1.route('/iniciar_sesion')
def iniciar():
	return "iniciar sesion"

@app1.route('/crear_usuario')
def crear():
	return "usuario: "

@app1.route('/crear_pagina')
def crear_perfil():
	return "creando el perfil"

@app1.route('/cerrar_sesion')
def cerrar_sesion():
	return 'se esta cerrando la sesion'

@app1.route('/ir_perfil')
def navegar_perfil():
	return "navengando a un perfil"

@app1.route('/ir_perfil_privado')
def navegar_perfil_privado():
	return "navegando privadamente"

if __name__ == '__main__':
	app1.run(host = '0.0.0.0', port = 8080)


