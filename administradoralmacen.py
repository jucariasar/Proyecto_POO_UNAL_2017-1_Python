from administrativo import Administrativo

class AdministradorAlmacen(Administrativo):
    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll="", email="", grado=0, 
    usuario="", password=""):
        super().__init__(ident, nombre, apellido, numElementPrest, roll, email, grado)
        self._usuario = usuario
        self._password = password
    def getUsuario(self):
        return self._usuario
    def setUsuario(self,usuario):
        self._usuario=usuario
        
    def getPassword(self):
        return self._Password
    def setPassword(self,password):
        self._password=password
        
    
    def __str__(self):
        retrun (super().__str__()+'\n'+"Usuario: "+self.getUsuario()+'\n'+"Password: "+self.getPassword())