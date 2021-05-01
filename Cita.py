class Cita:
    def __init__(self,idpaciente,hora,fecha,motivo,idcita):
        self.idpaciente=idpaciente
        self.hora=hora
        self.fecha=fecha
        self.motivo=motivo
        self.idcita=idcita
        self.estado='Pendiente'
    
    #  metodos get


    def getIdpaciente(self):
        return self.idpaciente

    def getHora(self):
        return self.hora

    def getFecha(self):
        return self.fecha

    def getMotivo(self):
        return self.motivo

    def getIdcita(self):
        return self.idcita

    def getEstado(self):
        return self.estado

    # Metodos set

    def setEstado(self,estado):
        self.estado=estado

