from flask import Flask,jsonify,request

from flask_cors import CORS

# importacion de las clases que manejaran los objetos
from Paciente import Paciente

import json

# creacion de arreglo de objetos necesarios

Pacientes=[]
cPacientes=0

app=Flask(__name__)
CORS(app)

Pacientes.append(Paciente("Angel","Barrera","23/11/00","M","angel2311","566621147",47450380,0))

@app.route('/mostrarpacientes',methods=['GET'])
def mostrarpacientes():
    global Pacientes
    datos=[]
    for paciente in Pacientes:
        objeto={
            'nombre':paciente.getNombre(),
            'apellido':paciente.getApellido(),
            'fecha':paciente.getFecha(),
            'sexo':paciente.getSexo(),
            'usuario':paciente.getUser(),
            'contraseña':paciente.getContraseña(),
            'telefono':paciente.getTelefono()
        }
        datos.append(objeto)
    return (jsonify(datos))

    


@app.route('/registrar',methods=['POST'])
def guardarpaciente():

    global Pacientes
    global cPacientes

    nombre=request.json['nombre']
    apellido=request.json['apellido']
    fecha=request.json['fecha']
    sexo=request.json['sexo']
    usuario=request.json['usuario']
    contraseña=request.json['contraseña']
    telefono=request.json['contraseña']

    for paciente in Pacientes:
        if usuario==paciente.getUser():
            return jsonify({'Mensaje':"El usuario ya existe, por favor ingrese uno diferente"})

    Pacientes.append(Paciente(nombre,apellido,fecha,sexo,usuario,contraseña,telefono,cPacientes))
    cPacientes+=1
    return jsonify({'Mensaje':"Su cuenta ha sido registrada con exito"})


    





if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)