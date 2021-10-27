from flask import Flask, render_template, request, make_response, jsonify, redirect
from flask.json import JSONEncoder
from flaskext.mysql import MySQL
from pymysql import cursors
from pymysql.cursors import Cursor
from werkzeug.wrappers import response
from config import config

# inicio de la app
app = Flask(__name__)
# Inicio para la conexion a la DB
conexion = MySQL(app)
# Routeo de paginas
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login")
def inventario():
    return render_template("login.html")
def paginanoencontrada(e):
    return "<h1>Error 404</h1><h2>La pagina que usted desea visualizar no existe o es incorrecta</h2>"

# Controladores
@app.route('/apiListarUsuarios')
def apiListarUsuarios():
    try:
        sql="SELECT * FROM dbdesire.usuarios where estado = '1'"
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        usuarios=[]
        for fila in datos:
            producto={'id':fila[0],'usuario':fila[1],'pass':fila[2]}
            usuarios.append(producto)
        conn.commit()
        return jsonify({'product':usuarios, 'mensaje':"correcto"})
    except:
        conn.commit()
        return jsonify({'mensaje':"Error en la base de datos"})
@app.route('/apiLogin', methods=['POST'])
def apiLogin():
    try: 
        sql="SELECT * FROM dbDesire.usuarios where usuario = '{0}' and pass = '{1}'".format(request.json['usuario'],request.json['pass'])
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)
        if not len(datos) == 0:
            return jsonify("Bienvenido")
        else:
            return jsonify("No existe el usuario o la contraseña es incorrecta")

    except:
        return jsonify("Error en la base de datos contacta con el administrador")
    

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,paginanoencontrada)
    app.run()
