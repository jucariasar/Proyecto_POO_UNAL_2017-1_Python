from empleado import Empleado

class Operario(Empleado):
	MAX_OP = 15 # Constante de clase para controlar el numero máximo de elementos que puede
				# prestar un operario
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, email, tipo):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
		self._tipo = tipo #Puede ser Mecanico, Electricista o Electrónico

	def getTipo(self):
		return self._tipo

	def setTipo(self, tipo):
		self._tipo = tipo

	def __str__(self):
		return(super().__str__() + "\nTipo: " + self.getTipo())