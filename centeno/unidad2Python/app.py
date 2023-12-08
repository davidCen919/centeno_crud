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
       app.config['MYSQL_DATABASE_USER']='root'
       app.config['MYSQL_DATABASE_PASSWORD']=''
       app.config['MYSQL_DATABASE_DB']='sitio'
       mysql.init_app(app)
#nuevo código

conn_db(app)

@app.route('/')
def inicio():
    # Conecta a la base de datos
    conexion=mysql.connect()
    # Realiza consultas para obtener productos de diferentes categorías
    cursor = conexion.cursor()
    cursor.execute("SELECT id,nombre, imagen, url FROM libros")
    libros = cursor.fetchall()
    # Realiza la consulta para obtener todos los juegos
    cursor.execute("SELECT id_juego, nombre, descripcion, url FROM juegos")
    juegos = cursor.fetchall()
    # Realiza la consulta para obtener todas las películas
    cursor.execute("SELECT id_pelicula, nombre, descripcion, url FROM peliculas")
    peliculas = cursor.fetchall()
    # Realiza la consulta para obtener todos los artículos
    cursor.execute("SELECT id_articulo, nombre, descripcion, url FROM articulos")
    articulos = cursor.fetchall()

    conexion.close()
    return render_template('sitio/index.html', libros=libros)
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
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM libros WHERE id=%s', (id,))
        data = cursor.fetchone()

        if data is None:
            # Handle the case where no data is found for the given ID
            return render_template('error.html', message='Libro no encontrado')

        if request.method == 'POST':
            nombre = request.form['nombre']
            imagen = request.form['imagen']
            url = request.form['url']
            
            cursor.execute('UPDATE libros SET nombre=%s, imagen=%s, url=%s WHERE id=%s', (nombre, imagen, url, id))
            mysql.get_db().commit()
            return redirect(url_for('libros'))

        return render_template('edit.html', data=data)
    except Exception as e:
        print(f"Error en edit_libro: {e}")
        abort(500, description=str(e))


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

#edit juegos
@app.route('/editjuegos/<int:id>', methods=['GET', 'POST'])
def editjuegos(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM juegos WHERE id=%s', (id,))
    libro = cursor.fetchone()
    if request.method == 'POST':
        nombre = request.form['nombre']
        imagen = request.form['imagen']
        url = request.form['url']
        # Agregar validación y procesamiento de datos aquí
        cursor.execute('UPDATE juegos SET nombre=%s, imagen=%s, url=%s WHERE id=%s', (nombre, imagen, url, id_juego))
        mysql.get_db().commit()
        return redirect(url_for('juegos'))
    columnas = [desc[0] for desc in cursor.description]
    libro = dict(zip(columnas, libro))
    return render_template('actions/juegos/edit.html', libro=libro)

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