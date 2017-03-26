from empleado import Empleado

class Administrativo(Empleado):
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, contador, email, grado):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, contador, email)
		self._grado = grado
	def getGrado (self):
		return self._grado
	def setGrado (self, grado):
		self._grado = grado