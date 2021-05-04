class Enfermedad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.cantidad=1
    
    #  metodos get


    def getNombre(self):
        return self.nombre

    def getCantidad(self):
        return self.cantidad

    # Metodos set

    def setNombre(self,nombre):
        self.nombre=nombre

    def setCantidad(self,cantidad):
        self.cantidad=cantidad