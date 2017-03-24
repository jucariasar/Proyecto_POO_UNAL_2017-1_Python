from empleado import Empleado

class IngenieroTecnico(Empleado):
	def __init__(self, ident, nombre, apellido, numElementPrest, roll, email, area):
		super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
		self._areaEncargada = area

	def getArea(self):
		return self._areaEncargada

	def setArea(self, area):
		self._areaEncargada = area

	def __str__(self):
		return (super().__str__() + "\nArea Encargada: " + self.getArea())
