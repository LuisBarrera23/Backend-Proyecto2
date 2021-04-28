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
            'telefono':paciente.getTelefono(),
            'id':paciente.getId()
        }
        datos.append(objeto)
    return (jsonify(datos))

@app.route('/paciente/<string:id>',methods=['GET'])
def mostrarpaciente(id):
    global Pacientes
    for paciente in Pacientes:
       if paciente.getId()==int(id):
            objeto={
            'nombre':paciente.getNombre(),
            'apellido':paciente.getApellido(),
            'fecha':paciente.getFecha(),
            'sexo':paciente.getSexo(),
            'usuario':paciente.getUser(),
            'contraseña':paciente.getContraseña(),
            'telefono':paciente.getTelefono(),
            'id':paciente.getId()
            }
            return (jsonify(objeto))
    


    


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
    telefono=request.json['telefono']

    for paciente in Pacientes:
        if usuario==paciente.getUser():
            return jsonify({'Mensaje':"El usuario ya existe, por favor ingrese uno diferente"})

    Pacientes.append(Paciente(nombre,apellido,fecha,sexo,usuario,contraseña,telefono,cPacientes))
    cPacientes+=1
    return jsonify({'Mensaje':"Su cuenta ha sido registrada con exito"})

@app.route('/eliminarpaciente/<int:id>',methods=['DELETE'])
def eliminarpaciente(id):
    global Pacientes

    for i in range(len(Pacientes)):
        if(Pacientes[i].getId()==id):
            del Pacientes[i]
            return jsonify({'Mensaje':'El usuario fue eliminado con exito'})
    
    return jsonify({'Mensaje':'No fue encontrado el usuario'})


@app.route('/actualizarpaciente', methods=['PUT'])
def actualizarpaciente():
    global Pacientes
    repetido=False
    for pacientes in Pacientes:
        if((request.json['usuario']==pacientes.getUser()) and (int(request.json['id'])==pacientes.getId())):
            repetido=False
        if((request.json['usuario']==pacientes.getUser()) and not(int(request.json['id'])==pacientes.getId())):
            repetido=True

    if(repetido==False):
        for i in range(len(Pacientes)):
            if(Pacientes[i].getId()==int(request.json['id'])):
                nombre=request.json['nombre']
                apellido=request.json['apellido']
                fecha=request.json['fecha']
                sexo=request.json['sexo']
                usuario=request.json['usuario']
                contraseña=request.json['contraseña']
                telefono=request.json['telefono']

                Pacientes[i].setNombre(nombre)
                Pacientes[i].setApellido(apellido)
                Pacientes[i].setFecha(fecha)
                Pacientes[i].setSexo(sexo)
                Pacientes[i].setUser(usuario)
                Pacientes[i].setContraseña(contraseña)
                Pacientes[i].setTelefono(telefono)
                return jsonify({'Mensaje':"Su perfil ha sido modificado"})
    else:
        return jsonify({'Mensaje':"Usuario repetido, por favor elija otro"})
    



            

    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)