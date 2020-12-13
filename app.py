from urllib import request
from flask import Flask, render_template, request
from utils import isEmailValid, isPasswordValid, isUsernameValid
import yagmail as yagmail

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('1.login.html')


#Registro Nuevo Usuario
@app.route('/RegistrarNuevoUsuario')
def RegistrarNuevoUsuario():
        return render_template('6.Registrar_Usuario.html')

#Menu User seleccionar producto para actualizar invetario
@app.route('/MenuUser')
def MenuUser():
        return render_template('3.Actualizar inventario.html')

#Menu User ctualizar inventario
@app.route('/MenuUserActualizarInvetario')
def MenuUserActualizarInvetario():
        return render_template('5.UpdInv.html')

#Menu Admin
@app.route('/MenuAdmin')
def MenuAdmin():
        return render_template('2.menuadmin2.html')


#Nuevo Prodcuto
@app.route('/NuevoProducto')
def NuevoProducto():
        return render_template('9.adminCrear2.html')


#Actualizar Producto busqueda
@app.route('/ActualizarProducto')
def ActualizarProducto():
        return render_template('10.ActualizarProducto.html')

#Actualizar Producto 2 parte
@app.route('/ActualizarProducto2')
def ActualizarProducto2():
        return render_template('11.actualizar2.html')


#Eliminar Prodcuto
@app.route('/EliminarProducto')
def EliminarProducto():
        return render_template('12.elminar1.html')

#Eliminar Prodcuto 2
@app.route('/EliminarProducto2')
def EliminarProducto2():
        return render_template('13.elminar2.html')


#Asignacion contraseña olvidada
@app.route('/AsignacionContrasseñaOlvidada2')
def AsignacionContrasseñaOlvidada2():
        return render_template('8.ConfirmarContraseña.html')


#verificacion login
@app.route('/procesarlogin', methods=['POST'])
def procesarlogin():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        #return 'hola ' + usuario
        men = ''
        if not isUsernameValid(usuario):
            #men += "Usuario no valido \n"
           # return men
            return render_template('1.login.html')
        #if not isPasswordValid(password):
            #men += "Contraseña no valida \n"
            #return men
        if men == '':
            #return 'BIENVENIDO'
            #men = "Ingreso Correcto"
            #return men
            return render_template('2.menuadmin2.html')


#Contraseña Olvidada
@app.route('/ContrasenaOlvidada')
def ContrasenaOlvidada():
        return render_template('7.recuperarContra.html')


#verificacion correo contraseña olvidada
@app.route('/VerificacionContrasenaOlvidada', methods=['POST'])
def VerificacionContrasenaOlvidada():
    if request.method == 'POST':
        email = request.form['email']
        men = ''
        if not isEmailValid(email):
            men += "Email no valido \n"
        if men == '':
            #return 'BIENVENIDO'
            #men = "Ingreso Correcto"
            #return men
            yag = yagmail.SMTP('correopruebatic2020@gmail.com', 'misiontic2020')
            yag.send(to=email, subject='Contraseña Olvidada', contents='Cambia tu contraseña <a href="http://127.0.0.1:5000/AsignacionContrasseñaOlvidada2">clic aqui</a>')
            return render_template('1.login.html')


#Asignacion contrasseña olvidada
@app.route('/AsignacionContrasseñaOlvidada', methods=['POST'])
def AsignacionContrasseñaOlvidada():
    if request.method == 'POST':
        password = request.form['password']
        men = ''
        # if not isPasswordValid(password):s
        # men += "Contraseña no valida \n"
        if men == '':
            #return 'BIENVENIDO'
            #men = "Ingreso Correcto"
            #return men

            return render_template('1.login.html')


#verificacion Registro Nuevo Usuario
@app.route('/procesar', methods=['POST'])
def procesar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        email = request.form['email']
        password = request.form['password']
        #return 'hola ' + usuario
        men = ''
        if not isUsernameValid(usuario):
            men += "Usuario no valido \n"
        #if not isPasswordValid(password):s
           # men += "Contraseña no valida \n"
        if not isEmailValid(email):
            men += "Email no valido \n"
        if men == '':
            #return 'BIENVENIDO'
            yag = yagmail.SMTP('correopruebatic2020@gmail.com', 'misiontic2020')
            yag.send(to=email, subject='Nueva Cuenta', contents='Activar cuenta <a href="www.google.com">clic aqui</a>')
            #men = "Ingreso Correcto"
            return render_template('2.menuadmin2.html')

#Creacion Nuevo Producto
@app.route('/ProcesarNuevoProdcuto', methods=['POST'])
def ProcesarNuevoProdcuto():
    if request.method == 'POST':
        producto = request.form['producto']
        cantidad = request.form['cantidad']
        #imagen = request.form['imagen']
        men = ''
       #   ¿Como valido el producto, la cantidad y la imagen?
        if men == '':
            return render_template('2.menuadmin2.html')

#Actualizar Producto
@app.route('/procesarActualizarProducto', methods=['POST'])
def procesarActualizarProducto():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        cantidad = request.form['Cantidad']
        men = ''
        if men == '':
            return render_template('2.menuadmin2.html')

#Actualizar Inventario Usuario
@app.route('/ActualizarInventarioUsuario', methods=['POST'])
def ActualizarInventarioUsuario():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        men = ''
        if men == '':
            return render_template('3.Actualizar inventario.html')


if __name__ == '__main__':
    app.run()
