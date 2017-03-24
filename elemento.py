from empleado import Empleado

class Elemento:
	def __init__(self, codigo, nombre, ubicacion, fechaPrestamo, contador, valor, estadoActual):
		self._codigo = codigo
		self._nombre = nombre
		self._ubicacion = ubicacion
		self._fechaPrestamo = fechaPrestamo
		self._contador = contador
		self._valor = valor
		self._estadoActual = estadoActual #Puede ser Disponible, Prestado o Reservado