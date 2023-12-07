from flask import Flask, render_template, request, redirect, url_for
from flask import render_template

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
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tu_tabla WHERE id=%s', (id,))
    data = cursor.fetchone()
    if request.method == 'POST':
        nombre = request.form['nombre']
        # Agregar validación y procesamiento de datos aquí
        cursor.execute('UPDATE libros SET nombre=%s WHERE id=%s', (nombre, id))
        mysql.get_db().commit()
        return redirect(url_for('index'))
    return render_template('edit.html', data=data)

@app.route('/delete/<int:id>')
def delete(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('DELETE FROM tu_tabla WHERE id=%s', (id,))
    mysql.get_db().commit()
    return redirect(url_for('index'))