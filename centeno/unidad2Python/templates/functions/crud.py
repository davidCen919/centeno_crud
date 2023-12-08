from flask import Flask, render_template, request, redirect, url_for
from flask import render_template
from flask import jsonify
from werkzeug.exceptions import abort

from app import conn_db
from app import mysql
from .. import app
app = Flask(__name__)

conn_db(app)

@app.route('/')
def index():
    try:
        cursor = mysql.get_db().cursor()

        # Consulta SQL para obtener registros de todas las tablas
        cursor.execute('SELECT id, nombre, imagen, url, "libros" as tipo FROM libros '
                       'UNION ALL '
                       'SELECT id_articulos, nombre, descripcion, url, "articulos" as tipo FROM articulos '
                       'UNION ALL '
                       'SELECT id_pelicula, nombre, descripcion, url, "peliculas" as tipo FROM peliculas '
                       'UNION ALL '
                       'SELECT id_juego, nombre, descripcio, url, "juegos" as tipo FROM juegos')

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


@app.route('/addlibross', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        # Agregar validación y procesamiento de datos aquí
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO libros (nombre) VALUES (%s)', (nombre,))
        mysql.get_db().commit()
        return redirect(url_for('index'))
    return render_template('../actions/libros/add.html')

@app.route('/editlibros/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM libros WHERE id=%s', (id,))
    libro = cursor.fetchone()

    if request.method == 'POST':
        # Procesa la solicitud de actualización del formulario
        nombre = request.form['nombre']
        imagen = request.form['imagen']
        url = request.form['url']
        # Agregar validación y procesamiento de datos aquí
        cursor.execute('UPDATE libros SET nombre=%s, imagen=%s, url=%s WHERE id=%s', (nombre, imagen, url, id))
        mysql.get_db().commit()
        return redirect(url_for('libros'))

    return render_template('actions/libros/edit.html', libro=libro)
    
@app.route('/delete/<int:id>')
def delete(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('DELETE FROM tu_tabla WHERE id=%s', (id,))
    mysql.get_db().commit()
    return redirect(url_for('index'))
