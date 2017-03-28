from empleado import Empleado

class Operario(Empleado):
	MAX_OP = 15 # Constante de clase para controlar el numero máximo de elementos que puede
				# prestar un operario
	tipo = {'1':'Mecanico', 
	'2':'Electrico', '3':'Electronico'} # Diccionario estatico para estandarizar los tipos de Operarios

	def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll="", email="", tipo=""):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
		self._tipo = tipo # Los tipos definidos en el diccionario estatico de tipo

	def getTipo(self):
		return self._tipo

	def setTipo(self, tipo):
		self._tipo = tipo

	def __str__(self):
		return(super().__str__() + "\nTipo: " + self.getTipo())