from administrativo import Administrativo

class AdministradorAlmacen(Administrativo):
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, contador, email, grado, 
	usuario, password):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, contador, email, grado)
		self._usuario = usuario
		self._password = password
