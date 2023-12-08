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
       cursor = mysql.get_db().cursor()
       cursor.execute('SELECT * FROM libros')
       libros = cursor.fetchall()
       return render_template('sitio/libros.html',libros=libros)


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

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    try:
        cursor = mysql.get_db().cursor()
        if request.method == 'POST':
            # Procesa la solicitud de actualización del formulario
            nombre = request.form['nombre']
            imagen = request.form['imagen']
            url = request.form['url']
            
            cursor.execute('UPDATE libros SET nombre=%s, imagen=%s, url=%s WHERE id=%s', (nombre, imagen, url, id))
            mysql.get_db().commit()
            return redirect(url_for('libros'))
        else:
            # Maneja la solicitud GET para obtener la información del libro
            cursor.execute('SELECT * FROM libros WHERE id=%s', (id,))
            data = cursor.fetchone()

            if data is None:
                # Maneja el caso en el que no se encuentre información para el ID dado
                return render_template('error.html', message='Libro no encontrado')

            return jsonify({
                'id': data[0],
                'nombre': data[1],
                'imagen': data[2],
                'url': data[3]
            })
    except Exception as e:
        print(f"Error en edit_libro: {e}")
        abort(500, description=str(e))
    
@app.route('/delete/<int:id>')
def delete(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('DELETE FROM tu_tabla WHERE id=%s', (id,))
    mysql.get_db().commit()
    return redirect(url_for('index'))