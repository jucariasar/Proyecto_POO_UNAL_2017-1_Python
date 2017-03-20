from empleado import Empleado

class Operario(Empleado):
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, contador, email, tipo):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, contador, email)
		self._tipo = tipo #Puede ser Mecanico, Electricista o Electrónico