from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask import render_template
from flask import abort

from pymysql.cursors import DictCursor
#importar la plantilla index.html
from flaskext.mysql import MySQL
#para crear nuestra aplicación
app = Flask(__name__)
#base de datos
#nuevo código para poder hacer una conexión a una base de datos
mysql=MySQL()

def conn_db(app):
       app.config['MYSQL_DATABASE_HOST']='localhost'
       app.config['MYSQL_DATABASE_USER']='sqluser'
       app.config['MYSQL_DATABASE_PASSWORD']='password'
       app.config['MYSQL_DATABASE_DB']='sitio2'
       mysql.init_app(app)
#nuevo código

conn_db(app)

@app.route('/')
def inicio():
    try:
        cursor = mysql.get_db().cursor()

        # Consulta SQL para obtener registros de todas las tablas
        cursor.execute('SELECT id, nombre, imagen, url, "libros" as tipo FROM libros '
                       'UNION ALL '
                       'SELECT id_articulo, nombre, descripcion, url, "articulos" as tipo FROM articulos '
                       'UNION ALL '
                       'SELECT id_pelicula, nombre, descripcion, url, "peliculas" as tipo FROM peliculas '
                       'UNION ALL '
                       'SELECT id_juego, nombre, descripcion, url, "juegos" as tipo FROM juegos')

        registros = cursor.fetchall()

        # Filtra los registros según la tabla a la que pertenecen
        libros = [registro for registro in registros if registro[4] == 'libros']
        articulos = [registro for registro in registros if registro[4] == 'articulos']
        peliculas = [registro for registro in registros if registro[4] == 'peliculas']
        juegos = [registro for registro in registros if registro[4] == 'juegos']

        return render_template('sitio/index.html', libros=libros, articulos=articulos, peliculas=peliculas, juegos=juegos)
    except Exception as e:
        print(f"Error en index: {e}")
        abort(500, description=str(e))
        # Maneja la excepción de manera adecuada según tus necesidades
    return render_template('error.html', message='Error en la aplicación')

#CREAR RUTAS
@app.route('/libros')
def libros():
       conexion=mysql.connect() #creamos la conexión con la base de datos
       cursor= conexion.cursor(DictCursor)
       cursor.execute("SELECT id, nombre, imagen, url FROM libros")
       libros=cursor.fetchall()
       conexion.commit()
       return render_template('sitio/libros.html',libros=libros)
@app.route('/peliculas')
def peliculas():
       conexion=mysql.connect() #creamos la conexión con la base de datos
       cursor= conexion.cursor(DictCursor)
       cursor.execute("SELECT id_pelicula, nombre, descripcion, url FROM peliculas")
       peliculas=cursor.fetchall()
       conexion.commit()
       return render_template('sitio/peliculas.html',peliculas=peliculas)
@app.route('/articulos')
def articulos():
       conexion=mysql.connect() #creamos la conexión con la base de datos
       cursor= conexion.cursor(DictCursor)
       cursor.execute("SELECT id_articulo, nombre, descripcion, url FROM articulos")
       articulos=cursor.fetchall()
       conexion.commit()
       return render_template('sitio/articulos.html',articulos=articulos)
@app.route('/juegos')
def juegos():
       conexion=mysql.connect() #creamos la conexión con la base de datos
       cursor= conexion.cursor(DictCursor)
       cursor.execute("SELECT id_juego, nombre, descripcion, url FROM juegos")
       juegos=cursor.fetchall()
       conexion.commit()
       return render_template('sitio/juegos.html',juegos=juegos)


#CRUD libros
@app.route('/addlibros', methods=['GET', 'POST'])
def addlibros():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            imagen = request.form['imagen']
            url = request.form['url']

            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO libros (nombre, imagen, url) VALUES (%s, %s, %s)', (nombre, imagen, url))
            mysql.get_db().commit()
            return redirect(url_for('libros'))
        except Exception as e:
            print(f"Error en addlibros: {e}")
            return jsonify({'error': str(e)}), 500
    return render_template('actions/libros/add.html')

#edit libro
@app.route('/editlibros/<int:id>', methods=['GET', 'POST'])
def editlibros(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM libros WHERE id=%s', (id,))
    libro = cursor.fetchone()

    if request.method == 'POST':
            nombre = request.form['nombre']
            imagen = request.form['imagen']
            url = request.form['url']
            
            cursor.execute('UPDATE libros SET nombre=%s, imagen=%s, url=%s WHERE id=%s', (nombre, imagen, url, id))
            mysql.get_db().commit()
            return redirect(url_for('libros'))
    columnas = [desc[0] for desc in cursor.description]
    libro = dict(zip(columnas,libro))
    return render_template('actions/libros/edit.html', libro=libro)


#eliminar libro
@app.route('/delete/<int:id>')
def delete(id):
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM libros WHERE id=%s', (id,))
        mysql.get_db().commit()
        return redirect(url_for('libros'))
    except Exception as e:
        print(f"Error en delete_libro: {e}")
        return jsonify({'error': str(e)}), 500


#CRUD peliculas
@app.route('/addpeliculas', methods=['GET', 'POST'])
def addpeliculas():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            url = request.form['url']

            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO peliculas (nombre, descripcion, url) VALUES (%s, %s, %s)', (nombre, descripcion, url))
            mysql.get_db().commit()
            return redirect(url_for('peliculas'))
        except Exception as e:
            print(f"Error en addpeliculas: {e}")
            return jsonify({'error': str(e)}), 500
    return render_template('actions/peliculas/add_peliculas.html')

#edit pelicula
@app.route('/editarpeliculas/<int:id>', methods=['GET', 'POST'])
def editpeliculas(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM peliculas WHERE id_pelicula=%s', (id,))
    pelicula = cursor.fetchone()

    if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            url = request.form['url']
            
            cursor.execute('UPDATE peliculas SET nombre=%s, descripcion=%s, url=%s WHERE id_pelicula=%s', (nombre, descripcion, url, id))
            mysql.get_db().commit()
            return redirect(url_for('libros'))
    columnas = [desc[0] for desc in cursor.description]
    pelicula = dict(zip(columnas,pelicula))
    return render_template('actions/peliculas/edit_peliculas.html', pelicula=pelicula)

#eliminar pelicula
@app.route('/deletePelicula/<int:id>')
def deletePelicula(id):
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM peliculas WHERE id_pelicula=%s', (id,))
        mysql.get_db().commit()
        return redirect(url_for('peliculas'))
    except Exception as e:
        print(f"Error en delete_pelicula: {e}")
        return jsonify({'error': str(e)}), 500
    
#CRUD articulo
@app.route('/addarticulos', methods=['GET', 'POST'])
def addarticulos():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            url = request.form['url']

            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO articulos (nombre, descripcion, url) VALUES (%s, %s, %s)', (nombre, descripcion, url))
            mysql.get_db().commit()
            return redirect(url_for('articulos'))
        except Exception as e:
            print(f"Error en addarticulos: {e}")
            return jsonify({'error': str(e)}), 500
    return render_template('actions/articulos/add_articulos.html')

#edit articulo
@app.route('/editarticulos/<int:id>', methods=['GET', 'POST'])
def editarticulos(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM articulos WHERE id_articulo=%s', (id,))
    articulo = cursor.fetchone()

    if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            url = request.form['url']
            
            cursor.execute('UPDATE articulos SET nombre=%s, descripcion=%s, url=%s WHERE id_articulo=%s', (nombre, descripcion, url, id))
            mysql.get_db().commit()
            return redirect(url_for('libros'))
    columnas = [desc[0] for desc in cursor.description]
    articulo = dict(zip(columnas,articulo))
    return render_template('actions/articulos/edit_articulos.html', articulo=articulo)

#eliminar articulos
@app.route('/deleteArticulo/<int:id>')
def deleteArticulo(id):
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM articulos WHERE id_articulo=%s', (id,))
        mysql.get_db().commit()
        return redirect(url_for('articulos'))
    except Exception as e:
        print(f"Error en delete_articulos: {e}")
        return jsonify({'error': str(e)}), 500
    
#CRUD juego
@app.route('/addjuegos', methods=['GET', 'POST'])
def addjuegos():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            url = request.form['url']

            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO juegos (nombre, descripcion, url) VALUES (%s, %s, %s)', (nombre, descripcion, url))
            mysql.get_db().commit()
            return redirect(url_for('juegos'))
        except Exception as e:
            print(f"Error en addjuegos: {e}")
            return jsonify({'error': str(e)}), 500
    return render_template('actions/juegos/add_juegos.html')

#edit pelicula
@app.route('/editarjuegos/<int:id>', methods=['GET', 'POST'])
def editjuegos(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM juegos WHERE id_juego=%s', (id,))
    juego = cursor.fetchone()

    if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            url = request.form['url']
            
            cursor.execute('UPDATE juegos SET nombre=%s, descripcion=%s, url=%s WHERE id_juego=%s', (nombre, descripcion, url, id))
            mysql.get_db().commit()
            return redirect(url_for('libros'))
    columnas = [desc[0] for desc in cursor.description]
    juego = dict(zip(columnas,juego))
    return render_template('actions/juegos/edit_juegos.html', juego=juego)

#eliminar articulos
@app.route('/deleteJuego/<int:id>')
def deleteJuego(id):
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM juegos WHERE id_juego=%s', (id,))
        mysql.get_db().commit()
        return redirect(url_for('juegos'))
    except Exception as e:
        print(f"Error en delete_juegos: {e}")
        return jsonify({'error': str(e)}), 500


if __name__=='__main__':
       app.run(debug=True)