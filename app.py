from logging import error
from flask import Flask, render_template, request, make_response, jsonify, redirect, session, escape, url_for
from flask.json import JSONEncoder
from flaskext.mysql import MySQL
from pymysql import cursors
from pymysql.cursors import Cursor
from werkzeug.wrappers import response
from config import config
# inicio de la app
app = Flask(__name__)
app.secret_key = "@112"
# Inicio para la conexion a la DB
conexion = MySQL(app)
# Routeo de paginas
@app.route("/")
def index():    
    return render_template("index.html")
@app.route("/login")
def login():
    if "usuario" in session:
        return render_template("cursos.html")
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.clear();
    return redirect(url_for("index"))
def paginanoencontrada(e):
    return "<h1>Error 404</h1><h2>La pagina que usted desea visualizar no existe o es incorrecta</h2>"
@app.route('/registrar')
def registrar():
    if "usuario" in session:
        return render_template("cursos.html")
    return render_template("registrar.html")
@app.route('/video')
def panel():
    return render_template("Videos.html")
@app.route('/cursos')
def cursos():
    try:
        
        sql="SELECT usuarios.usuario, usuarios.nombres, usuarios.apellidos, usuarios.correo, usuarios.telefono, cursos.curso, cursos.descripcion, cursos.precio, rol.rol, nivel.nivel, cursos.idcursos FROM (rol INNER JOIN usuarios ON rol.idrol = usuarios.fkrol) INNER JOIN (nivel INNER JOIN cursos ON nivel.idnivel = cursos.fknivel) ON usuarios.id = cursos.fkprofesor ;"
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursosTotal=[]
        for fila in datos:
            producto={'usuario':fila[0],'nombres':fila[1],'apellidos':fila[2],'correo':fila[3],'telefono':fila[4],'curso':fila[5],'descripcion':fila[6],'precio':fila[7],'rol':fila[8],'nivel':fila[9], 'idcurso' :fila[10]}
            cursosTotal.append(producto)
        conn.commit()

        if "usuario" in session:
            sql="SELECT usuarios.usuario, usuarios.nombres, usuarios.apellidos, usuarios.correo, usuarios.telefono, cursos.curso, cursos.descripcion, cursos.precio, rol.rol, nivel.nivel, cursos.idcursos FROM (rol INNER JOIN usuarios ON rol.idrol = usuarios.fkrol) INNER JOIN (nivel INNER JOIN cursos ON nivel.idnivel = cursos.fknivel) ON usuarios.id = cursos.fkprofesor WHERE usuarios.usuario='"+session["usuario"]+"' ;"
            conn = conexion.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            datos=cursor.fetchall()
            cursos=[]
            for fila in datos:
                producto={'usuario':fila[0],'nombres':fila[1],'apellidos':fila[2],'correo':fila[3],'telefono':fila[4],'curso':fila[5],'descripcion':fila[6],'precio':fila[7],'rol':fila[8],'nivel':fila[9], 'idcurso' :fila[10]}
                cursos.append(producto)
            conn.commit()

            sql1="SELECT a.id, a.usuario,c.curso,d.nivel,e.nombres  FROM usuarios a INNER JOIN cursoalumno b on a.id=b.fkusuario INNER JOIN cursos c on b.fkcurso = c.idcursos INNER JOIN nivel d on c.fknivel=d.idnivel INNER JOIN usuarios e on c.fkprofesor=e.id WHERE a.usuario='"+ session["usuario"] +"' "
            conn = conexion.connect()
            cursor = conn.cursor()
            cursor.execute(sql1)
            datos=cursor.fetchall()
            cursoalumno=[]
            for fila in datos:
                producto={'id':fila[0],'usuario':fila[1],'curso':fila[2],'nivel':fila[3],'nombres':fila[4]}
                cursoalumno.append(producto)
            conn.commit()
            return render_template("Cursos.html",curso=cursosTotal,cursoalumnos=cursoalumno,cursoprofe=cursos)
        else:
            return render_template("Cursos.html",curso=cursosTotal)        
    except:
        conn.commit()
        return jsonify({'mensaje':"Error en la base de datos"})
        
@app.route('/curso')    
def curso():

    curse = request.args.get('curso', 'No tienes permiso para acceder')
    idcurse = request.args.get('idcurse', 'Sin respuesta')
    if not idcurse == "":
        #Aca capturamos los datos generales del curso
        sql="SELECT * FROM dbdesire.cursos where idcursos = {};".format(idcurse)
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        curso=[]
        if not len(datos) == 0: 
            for fila in datos:
                item={'idcurso':fila[0],'curso':fila[1],'descripcion':fila[2]}
                curso.append(item)
            conn.commit()
        #Aca capturamos las urls del curso
            sql="SELECT modulocurso.idmodulocurso, modulocurso.url, modulocurso.descripcion FROM cursos INNER JOIN modulocurso ON cursos.idcursos = modulocurso.fkcursomodulo WHERE cursos.idcursos = '{}';".format(idcurse)
            conn = conexion.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            datos=cursor.fetchall()
            urlvideo=[]
            for filavideo in datos:
                video={'idmodulo':filavideo[0],'url':filavideo[1], 'descripcion':filavideo[2]}
                urlvideo.append(video)
            conn.commit()
        #Aca capturamos los pdf por modulo
            sql="SELECT modulocurso.idmodulocurso, archivoscurso.urlpdf FROM (cursos INNER JOIN modulocurso ON cursos.idcursos = modulocurso.fkcursomodulo) INNER JOIN archivoscurso ON modulocurso.idmodulocurso = archivoscurso.fkmodulocurso WHERE cursos.idcursos = '{}';".format(idcurse)
            conn = conexion.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            datos=cursor.fetchall()
            urlpdf=[]
            for filapdf in datos:
                pdf={'idmodulocurso':filapdf[0],'url':filapdf[1]}
                urlpdf.append(pdf)
            conn.commit()   
        return render_template("Videos.html", curso = curso, urlvideo = urlvideo, urlpdf = urlpdf)
        
@app.route('/inicio')
def inicio():
    return render_template("inicio.html")    
# Controladores
@app.route('/apiLogin', methods=['POST', 'GET'])
def apiLogin():
    try: 
        sql="SELECT * FROM dbDesire.usuarios where (usuario = '{0}' or correo = '{0}' or telefono= '{0}') and pass = '{1}'".format(request.json['usuario'],request.json['pass'])
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()        
        if not len(datos) == 0:
            session["usuario"]= datos[0][1]
            session["nombre"]= datos[0][3]
            session["rol"]= datos[0][7]
            return jsonify("Bienvenido")
        else:
            return jsonify("No existe el usuario o la contraseña es incorrecta")
    except:
        return jsonify("Error en la base de datos contacta con el administrador")
@app.route('/apiSearchUsuario', methods=['POST'])
def apiSearchUsuario():
    try:
        sql="SELECT usuario FROM dbDesire.usuarios where usuario = '{0}'".format(request.json['usuario'])
        print(sql)
        conn = conexion.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)              
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

        if resUsuario['success'] and resCorreo['success'] and resTelefono['success'] != True:
            sql = """INSERT INTO dbDesire.usuarios (usuario, pass, nombres, apellidos, correo, telefono, fkrol, estado) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}','1','1');""".format(request.json['usuario'],request.json['pass'],request.json['nombres'],request.json['apellidos'],request.json['correo'],request.json['telefono'])
            conn = conexion.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            return jsonify("Registro correcto")
        else:
            return jsonify(resUsuario['msj'],resCorreo['msj'],resTelefono['msj'])

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