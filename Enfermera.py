class Enfermera:
    def __init__(self,nombre,apellido,fecha,sexo,user,contraseña,telefono,id):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha=fecha
        self.sexo=sexo
        self.user=user
        self.contraseña=contraseña
        self.telefono=telefono
        self.id=id
    

    #  metodos get


    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getFecha(self):
        return self.fecha
    
    def getSexo(self):
        return self.sexo
    
    def getUser(self):
        return self.user
    
    def getContraseña(self):
        return self.contraseña
    
    def getTelefono(self):
        return self.telefono
        
    def getId(self):
        return self.id
    
    # Metodos set

    def setNombre(self,nombre):
        self.nombre=nombre

    def setApellido(self,apellido):
        self.apellido=apellido
    
    def setFecha(self,fecha):
        self.fecha=fecha

    def setSexo(self,sexo):
        self.sexo=sexo
    
    def setUser(self,user):
        self.user=user
    
    def setContraseña(self,contraseña):
        self.contraseña=contraseña
    
    def setTelefono(self,telefono):
        self.telefono=telefono

    def setId(self,id):
        self.id=id