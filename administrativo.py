

class Administrativo(Empleado):
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, contador, email, grado):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, contador, email)
		self._grado = grado
