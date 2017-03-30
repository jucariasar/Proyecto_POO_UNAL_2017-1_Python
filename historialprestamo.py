from empleado import Empleado
from elemento import Elemento

class HistorialPrestamo:
    def __init__(self, idEmpleado, nomEmpleado, nomElemento, codElemento, 
    fechaPrestamo, fechaDevolucion):
        self._idEmpleado = idEmpleado
        self._nomEmpleado = nomEmpleado
        self._nomElemento = nomElemento
        self._codElemento = codElemento
        self._fechaPrestamo = fechaPrestamo
        self._fechaDevolucion = fechaDevolucion
        
    def getIdEmpleado(self):
        return self._idEmpleado
    def setIdEmpleado(self,ident):
        self._idEmpleado=ident
        
    def getNomEmpleado(self):
        return self._nomEmpleado
    def setNomEmpleado(self,nom):
        self._nomEmpleado=nom
        
    def getNomElemento(self):
        return self._nomElemento
    def setNomElemento(self,nom):
        self._nomElemento=nom
                
    def getCodElemento(self):
        return self._codElemento
    def setCodElemento(self,cod):
        self._codElemento=cod
        
    def getFechaPrestamo(self):
        return self._fechaPrestamo
    def setFechaPrestamo(self,fechaP):
        self._fechaPrestamo=fechaP

    def getFechaDevolucion(self):
        return self._fechaDevolucion
    def setFechaDevolucion(self,fechaD):
        self._fechaDevolucion=fechaD

    def __str__(self):
        retrun ("Nombre del Empleado: " + self.getNomEmpleado() + '\n' +
         "N° Identificacion: " + str(self.getIdEmpleado()) + '\n' + 
         "Nombre del Elemento: " + self.getNomElemento() + '\n' + "Codigo Elemento: " + 
         str(self.getCodElemento()) + '\n' + "Fecha Prestamo: " + 
         str(self.getFechaPrestamo()) + '\n' + "Fecha Devolucion: " + str(self.getFechaDevolucion()))
        
