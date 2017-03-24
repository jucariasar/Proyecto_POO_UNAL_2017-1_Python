from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
#from historialprestamo import HistorialPrestamo

class Almacen:
	def __init__(self):
		self._empleados = []
		self._elementos = []
		self._historial = []

e1 = IngenieroTecnico(123, "Carlos", "Mesa", 3, "Ingeniero Tecnico", "cm@empresa.com", "Produccion")
e2 = Operario(321, "Alberto", "Henao", 4, "Operario", "ah@empresa.com", "Mecanico")

print(e1)
print("\n%s" % e2)
