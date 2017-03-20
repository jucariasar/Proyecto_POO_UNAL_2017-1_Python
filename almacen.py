from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from historialprestamo import HistorialPrestamo

class Almacen:
	def __init__(self):
		self._empleados = []
		self._elementos = []
		self._historial = []