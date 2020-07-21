from empleado import Empleado
from datetime import datetime, date, time, timedelta
import calendar

class HistorialPrestamo:
    historial = []
    def __init__(self, idEmpleado=0, nomEmpleado="", nomElemento="", codElemento=0, 
    fechaPrestamo=None, fechaDevolucion=None):
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
        if self.getFechaDevolucion() == None:
            self._fechaDevolucion = "Elemento Prestado"
        else:
            self._fechaDevolucion=fechaD

    def __str__(self):
        return ("\n Nombre del Empleado: " + self.getNomEmpleado() + '\n' +
         " N° Identificacion: " + str(self.getIdEmpleado()) + '\n' + 
         " Nombre del Elemento: " + self.getNomElemento() + '\n' + " Codigo Elemento: " + 
         str(self.getCodElemento()) + '\n' + " Fecha Prestamo: " + 
         str(self.getFechaPrestamo()) + '\n' + " Fecha Devolucion: " + str(self.getFechaDevolucion()))

    @staticmethod
    def agregarAHistorial(emp, element):
        h = HistorialPrestamo()
        h.setIdEmpleado(emp.getIdent())
        h.setNomEmpleado(emp.getNombre())
        h.setNomElemento(element.getDescripcion())
        h.setCodElemento(element.getCodigo())
        h.setFechaDevolucion(None)
        h.setFechaPrestamo(element.getFechaPrestamo())
        HistorialPrestamo().historial.append(h)

    @staticmethod
    def agregarFechaEntrega(emp, elemento):
        for h in HistorialPrestamo().historial:
            if elemento.getFechaPrestamo() == h.getFechaPrestamo() and emp.getIdent() == h.getIdEmpleado():
                h.setFechaDevolucion(datetime.now())

    @staticmethod
    def mostrarHistorial():
        for h in HistorialPrestamo().historial:
            print("%s \n" % h)