import re
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
@app.route('/registrar')
def registrar():
    return render_template("registrar.html")
@app.route('/panel')
def panel():
    return render_template("panel.html")
@app.route('/curso')
def curso():
    return render_template("Curso.html")
        
@app.route('/inicio')
def inicio():
    return render_template("inicio.html")    
# Controladores
@app.route('/apiLogin', methods=['POST'])
def apiLogin():
    try: 
        sql="SELECT * FROM dbDesire.usuarios where usuario = '{0}' and pass = '{1}'".format(request.json['usuario'],request.json['pass'])
        print(sql)
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        if not len(datos) == 0:
            return jsonify("Bienvenido")
        else:
            return jsonify("No existe el usuario o la contraseña es incorrecta")

    except:
        return jsonify("Error en la base de datos contacta con el administrador")
@app.route('/apiSearchUsuario', methods=['POST'])
def apiSearchUsuario():
    try:
        sql="SELECT usuario FROM dbDesire.usuarios where usuario = '{0}'".format(request.json['usuario'])
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()              
        if not len(datos) == 0:
            return {"success" : True, "msj": "Usuario ya existe"}
        else:
            return {"success" : False, "msj": "ok"}    
    except Exception as ex:
            raise ex
def apileerUsuario(user):
    try: 
        sql="SELECT usuario FROM dbDesire.usuarios where usuario = '{0}'".format(user)
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()              
        if not len(datos) == 0:
            return {"success" : True, "msj": "Usuario ya existe"}
        else:
            return {"success" : False, "msj": "ok"}
    except Exception as ex:
        raise ex
@app.route('/apiSearchCorreo', methods=['POST'])
def apiSearchCorreo():
    try:
        sql="SELECT correo FROM dbDesire.usuarios where correo = '{0}'".format(request.json['correo'])
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()              
        if not len(datos) == 0:
            return {"success" : True, "msj": "Correo ya registrado"}
        else:
            return {"success" : False, "msj": "ok"}
    except Exception as ex:
        raise ex
def apileerCorreo(correo):
    try: 
        sql="SELECT correo FROM dbDesire.usuarios where correo = '{0}'".format(correo)
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()              
        if not len(datos) == 0:
            return {"success" : True, "msj": "Correo ya registrado"}
        else:
            return {"success" : False, "msj": "ok"}
    except Exception as ex:
        raise ex
@app.route('/apiSearchTelefono', methods=['POST'])
def apiSearchTelefono():
    try: 
        sql="SELECT telefono FROM dbDesire.usuarios where telefono = '{0}'".format(request.json['telefono'])
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()              
        if not len(datos) == 0:
            return {"success" : True, "msj": "El numero telefonico ya fue registrado"}
        else:
            return {"success" : False, "msj": "ok"}
    except Exception as ex:
        raise ex
def apileerTelefono(telefono):
    try: 
        sql="SELECT telefono FROM dbDesire.usuarios where telefono = '{0}'".format(telefono)
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()              
        if not len(datos) == 0:
            return {"success" : True, "msj": "El numero telefonico ya fue registrado"}
        else:
            return {"success" : False, "msj": "ok"}
    except Exception as ex:
        raise ex

@app.route('/apiRegistro', methods=['POST'])
def apiRegistro():
    try:
        resUsuario = apileerUsuario(request.json['usuario'])
        resCorreo = apileerCorreo(request.json['correo'])
        resTelefono = apileerTelefono(request.json['telefono'])

        if resUsuario['success'] & resCorreo['success'] & resTelefono['success'] != True:
            sql = """INSERT INTO dbDesire.usuarios (usuario, pass, nombres, apellidos, correo, telefono, fkrol, estado) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}','1','1');""".format(request.json['usuario'],request.json['pass'],request.json['nombres'],request.json['apellidos'],request.json['correo'],request.json['telefono'])
            conn = conexion.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            return jsonify("Registro correcto")
        else:
            return jsonify("Esto no deberia de salir porq ya estamos validando en las apis xd y no deberias poder verlo")

    except Exception as ex:
            raise ex


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


if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,paginanoencontrada)
    app.run()