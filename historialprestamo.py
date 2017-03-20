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
