from flask import Flask,jsonify,request

from flask_cors import CORS

# importacion de las clases que manejaran los objetos
from Paciente import Paciente
from Doctor import Doctor
from Enfermera import Enfermera
from Medicamento import Medicamento

import json

# creacion de arreglo de objetos necesarios

Pacientes=[]
cPacientes=0

Doctores=[]
cDoctores=0

Enfermeras=[]
cEnfermeras=0

Medicamentos=[]
cMedicamentos=0

app=Flask(__name__)
CORS(app)



#Metodos de rutas necesarias para pacientes -----------------------------------------------------------------
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
    
#Fin de metodos de rutas para pacientes ---------------------------------------------------------------------

#Metodos de rutas necesarias para medicos -----------------------------------------------------------------
@app.route('/registrardoctor',methods=['POST'])
def guardardoctor():

    global Doctores
    global cDoctores

    nombre=request.json['nombre']
    apellido=request.json['apellido']
    fecha=request.json['fecha']
    sexo=request.json['sexo']
    usuario=request.json['usuario']
    contraseña=request.json['contraseña']
    especialidad=request.json['especialidad']
    telefono=request.json['telefono']

    for doctor in Doctores:
        if usuario==doctor.getUser():
            return jsonify({'Mensaje':"El usuario ya existe, por favor ingrese uno diferente"})

    Doctores.append(Doctor(nombre,apellido,fecha,sexo,usuario,contraseña,especialidad,telefono,cDoctores))
    cDoctores+=1
    return jsonify({'Mensaje':"Su cuenta ha sido registrada con exito"})

@app.route('/mostrarmedicos',methods=['GET'])
def mostrarmedicos():
    global Doctores
    datos=[]
    for doctor in Doctores:
        objeto={
            'nombre':doctor.getNombre(),
            'apellido':doctor.getApellido(),
            'fecha':doctor.getFecha(),
            'sexo':doctor.getSexo(),
            'usuario':doctor.getUser(),
            'contraseña':doctor.getContraseña(),
            'especialidad':doctor.getEspecialidad(),
            'telefono':doctor.getTelefono(),
            'id':doctor.getId()
        }
        datos.append(objeto)
    return (jsonify(datos))

@app.route('/doctor/<string:id>',methods=['GET'])
def mostrardoctor(id):
    global Doctores
    for doctor in Doctores:
       if doctor.getId()==int(id):
            objeto={
            'nombre':doctor.getNombre(),
            'apellido':doctor.getApellido(),
            'especialidad':doctor.getEspecialidad(),
            'fecha':doctor.getFecha(),
            'sexo':doctor.getSexo(),
            'usuario':doctor.getUser(),
            'contraseña':doctor.getContraseña(),
            'telefono':doctor.getTelefono(),
            'id':doctor.getId()
            }
            return (jsonify(objeto))

@app.route('/eliminardoctor/<int:id>',methods=['DELETE'])
def eliminardoctor(id):
    global Doctores

    for i in range(len(Doctores)):
        if(Doctores[i].getId()==id):
            del Doctores[i]
            return jsonify({'Mensaje':'El usuario fue eliminado con exito'})
    
    return jsonify({'Mensaje':'No fue encontrado el usuario'})

@app.route('/actualizarmedico', methods=['PUT'])
def actualizarmedico():
    global Doctores
    repetido=False
    for doctor in Doctores:
        if((request.json['usuario']==doctor.getUser()) and (int(request.json['id'])==doctor.getId())):
            repetido=False
        if((request.json['usuario']==doctor.getUser()) and not(int(request.json['id'])==doctor.getId())):
            repetido=True

    if(repetido==False):
        for i in range(len(Doctores)):
            if(Doctores[i].getId()==int(request.json['id'])):
                nombre=request.json['nombre']
                apellido=request.json['apellido']
                especialidad=request.json['especialidad']
                fecha=request.json['fecha']
                sexo=request.json['sexo']
                usuario=request.json['usuario']
                contraseña=request.json['contraseña']
                telefono=request.json['telefono']

                Doctores[i].setNombre(nombre)
                Doctores[i].setApellido(apellido)
                Doctores[i].setEspecialidad(especialidad)
                Doctores[i].setFecha(fecha)
                Doctores[i].setSexo(sexo)
                Doctores[i].setUser(usuario)
                Doctores[i].setContraseña(contraseña)
                Doctores[i].setTelefono(telefono)
                return jsonify({'Mensaje':"Su perfil ha sido modificado"})
    else:
        return jsonify({'Mensaje':"Usuario repetido, por favor elija otro"})
#Fin de metodos de rutas para medicos ---------------------------------------------------------------------
            

    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)