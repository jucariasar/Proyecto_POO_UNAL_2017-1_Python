from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from historialprestamo import HistorialPrestamo
import sys

class Almacen:
    def __init__(self):
        self._empleados = []
        self._elementos = []
        self._historial = []
        self._seleccion ={
        "1":self.crearDatosFicticios,
        "2":self.ingresarAlSistema,
        "3":self.salir
        }

    def crearDatosFicticios(self):
    	e1 = AdministradorAlmacen()
    	e2 = AdministradorAlmacen()

    def ingresarAlSistema(self):
    	pass

    def salir(self):
    	print("Muchas gracias por utilizar la aplicacion")
    	sys.exit(0)



    # Primer menu
    def menu(self):
    	break_while = 1
    	while break_while == 1:

    		print("")
    		print("1. Crear Datos Ficticios.")
    		print("2. Ingresar al sistema.")
    		print("3. Salir.")
    		op = input("\nIngrese la opcion deseada: ")
    		accion = self._seleccion.get(op)
    		if(accion):
    			accion()
    		else:
    			print("%s %s" % (op, "No es una opcion valida"))



if __name__ == "__main__":
	a = Almacen()
	a.menu()