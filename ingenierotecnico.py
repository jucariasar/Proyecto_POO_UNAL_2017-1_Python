from empleado import Empleado

class IngenieroTecnico(Empleado):
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, contador, email, area):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, contador, email)
		self._area = area
