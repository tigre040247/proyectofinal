#importa libreria
from wsgiref.simple_server import WSGIRequestHandler
from flask import Flask, render_template, redirect, request, url_for 


# Este es el nombre para llamar a los templates de python
app = Flask(__name__, template_folder='templates')


# Este es el arreglo para almacenar en nuestra informacion 
ListasAlmacenar = []  # Esta es para la lista al instante y Domicilio
# ---------------------------------------------------------------------------
# Password para tener acceso a dicha aplicacion mediante el uso del secret key
app.secret_key = 'covid123456'

# ---------------------------------------------------------------------------
# Inicializamos la ruta principal

@app.route('/')
def inicio():
    return render_template('/inicio.html', ListasAlmacenar=ListasAlmacenar)

# Inicializamos la ruta secundaria que es el inicio de nuestra aplicacion


@app.route('/informacion')
def informacion():
    return render_template('/informacion.html', ListasAlmacenar=ListasAlmacenar)

# Inicializamos la ruta 
@app.route('/salud')
def salud():
    return render_template('/salud.html', ListasAlmacenar=ListasAlmacenar)

# Inicializamos la ruta 
@app.route('/recomendaciones')
def recomendaciones():
    return render_template('/recomendaciones.html',ListasAlmacenar=ListasAlmacenar)

# Inicializamos la ruta 
@app.route('/vacunas')
def vacunas():
    return render_template('/vacunas.html', ListasAlmacenar=ListasAlmacenar)

# Inicializamos la ruta 
@app.route('/contacto')
def contacto():
    return render_template('/contacto.html', ListasAlmacenar=ListasAlmacenar)


#cpdogp hrml verficiacion de los servicios 
@app.route('/registro')
def registro():
    return render_template('/registro.html', ListasAlmacenar=ListasAlmacenar)


#ingreso registro de las vacunas 
@app.route('/datosregistro')
def datosregistro():
    return render_template('/datosregistro.html', ListasAlmacenar=ListasAlmacenar)

@app.route('/enviar', methods=['POST'])

def enviar():  
    if request.method == 'POST':
        
        Dato_Nombre = request.form['Dato_Nombre']
        Dato_Apellido = request.form['Dato_Apellido']
        Dato_Dosis = request.form['Dato_Dosis']
        Dato_Fecha = request.form['Dato_Fecha']

       
        if Dato_Nombre == '' or Dato_Apellido == '' or Dato_Dosis == '' or Dato_Fecha == '' :
            return redirect(url_for('datosregistro'))
        else:
            ListasAlmacenar.append({'Dato_Nombre': Dato_Nombre, 'Dato_Apellido': Dato_Apellido, 'Dato_Dosis': Dato_Dosis, 'Dato_Fecha': Dato_Fecha})
            return redirect(url_for('datosregistro'))



@app.route('/borrar', methods=['POST'])
def borrar():              # La funcion de envio de mensaje borrado se hace mediante codigo Javascript
    ListasAlmacenar.clear()
    return redirect(url_for('datosregistro'))



# ejecutar del main principal de la pagina To DO local host - version final del proyecto
if __name__ == '__main__':
    app.run(debug=True)