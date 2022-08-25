#Esto es un comentario
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pythonflaskweb'

mysql = MySQL(app)

@app.route('/') #Manejador de las rutas
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():    
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
    return 'Recibido'

@app.route('/edit')
def edit_contact():
    return "edit contact"

@app.route('/delete')
def delete_contact():
    return "delete contact"





#Parametros:
# Port: Puerto a utilizar.  Debug: Reinicia el servidor cada vez que hagamos cambios
if __name__ == '__main__':
  app.run(port= 3000, debug = True) #Inicia el servidor