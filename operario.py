from empleado import Empleado

class Operario(Empleado):
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, email, tipo):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
		self._tipo = tipo #Puede ser Mecanico, Electricista o Electrónico

	def getTipo(self):
		return self._tipo

	def setTipo(self, tipo):
		self._tipo = tipo

	def __str__(self):
		return(super().__str__() + "\nTipo: " + self.getTipo())