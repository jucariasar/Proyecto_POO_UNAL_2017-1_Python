from empleado import Empleado

class Administrativo(Empleado):
    MAX_AD = 5
    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll="", email="", grado=0):
        super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
        self._grado = grado
    def getGrado (self):
        return self._grado
    def setGrado (self, grado):
        self._grado = grado
    def __str__(self):
        return (super().__str__()+'\n'+ "Grado: "+ self.getGrado())
        