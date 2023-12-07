from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask import render_template
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
       app.config['MYSQL_DATABASE_DB']='sitio1'
       mysql.init_app(app)
#nuevo código

conn_db(app)

@app.route('/')
def inicio():
        return render_template('sitio/index.html')
#CREAR RUTAS
@app.route('/libros')
def libros():
       conexion=mysql.connect() #creamos la conexión con la base de datos
       cursor= conexion.cursor()
       cursor.execute("SELECT * FROM `libros`")
       libros=cursor.fetchall()
       conexion.commit()
       return render_template('sitio/libros.html',libros=libros)
@app.route('/peliculas')
def peliculas():
       return render_template('sitio/peliculas.html')
@app.route('/articulos')
def articulos():
       return render_template('sitio/articulos.html')
@app.route('/juegos')
def juegos():
       return render_template('sitio/juegos.html')


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
@app.route('/edit/<int:id>', methods=['GET', 'PUT'])
def edit(id):
    cursor = mysql.get_db().cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM libros WHERE id=%s', (id,))
        data = cursor.fetchone()
        return render_template('edit.html', data=data)

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            nombre = data['nombre']
            imagen = data['imagen']
            url = data['url']

            cursor.execute('UPDATE libros SET nombre=%s, imagen=%s, url=%s WHERE id=%s',
                           (nombre, imagen, url, id))
            mysql.get_db().commit()
            return jsonify({'message': 'Libro actualizado exitosamente'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

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

if __name__=='__main__':
       app.run(debug=True)