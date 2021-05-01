class Cita:
    def __init__(self,idpaciente,hora,fecha,motivo,idcita):
        self.idpaciente=idpaciente
        self.hora=hora
        self.fecha=fecha
        self.motivo=motivo
        self.idcita=idcita
        self.estado='Pendiente'
        self.doctor=''
        self.iddoctor=-1
    
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

    def getDoctor(self):
        return self.doctor

    def getIddoctor(self):
        return self.iddoctor

    # Metodos set

    def setEstado(self,estado):
        self.estado=estado

    def setDoctor(self,doctor):
        self.doctor=doctor

    def setIddoctor(self,iddoctor):
        self.iddoctor=iddoctor

