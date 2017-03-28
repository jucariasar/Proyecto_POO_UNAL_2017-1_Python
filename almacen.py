from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from historialprestamo import HistorialPrestamo
import sys
import os


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

    def ingresarAlSistema(self):
    	email = input("Ingrese su E-mail: ")
    	cc = int(input("Ingrese su Documento: "))

    	empTemp = Empleado().buscarEmpleadoPorId(self._empleados, cc)
        
    	if empTemp != None and isinstance(empTemp, AdministradorAlmacen):
            if(empTemp.getEmail() == email):
                self.menuAdministradorAlmacen(empTemp)
	elif (empTemp != None and isinstance(empTemp, Empleado):
	    if(empTemp.getEmail() == email):
	        self.menuEmpleado(empTemp)


    def menuAdministradorAlmacen(self, admin):
        print("\nBienvenido %s %s\n" % (admin.getNombre(), admin.getApellido()))
        print("Ingrese su Usuario y despues su Contraseña")
        user = input("Ingrese su Usuario: ")
        paswd = input("Ingrese su Contraseña: ")

    def menuEmpleado(self, admin):
        print("\nBienvenido %s %s\n" % (admin.getNombre(), admin.getApellido()))
        print("1. Consultar Elementos Disponibles.")
        print("2. Consultar Elementos Prestados.")
        print("3. Reservar Elementos para Prestar.")
        print("4. Modificar Reserva de Elementos.")
        print("5. Cancelar Reserva de Elementos.")

    def crearDatosFicticios(self):

    	e1 = AdministradorAlmacen()
    	e1.setIdent(1)
    	e1.setNombre("Pablo")
    	e1.setApellido("Castrillon")
    	e1.setNumElementPres(0)
    	e1.setRoll(Empleado().tiposEmpleado['1'])
    	e1.setEmail("pc@unal.edu.co")
    	e1.setGrado(10)
    	e1.setUsuario("pcastrillon")
    	e1.setPassword("1234")
    	self._empleados.append(e1)

    	e2 = AdministradorAlmacen()
    	e2.setIdent(2)
    	e2.setNombre("Jaider")
    	e2.setApellido("Peralta")
    	e2.setNumElementPres(0)
    	e2.setRoll(Empleado().tiposEmpleado['1'])
    	e2.setEmail("jp@unal.edu.co")
    	e2.setGrado(10)
    	e2.setUsuario("jperalta")
    	e2.setPassword("4567")
    	self._empleados.append(e2)

    	e3 = Administrativo()
    	e3.setIdent(3)
    	e3.setNombre("Yeison")
    	e3.setApellido("Ortiz")
    	e3.setNumElementPres(0)
    	e3.setRoll(Empleado().tiposEmpleado['2'])
    	e3.setEmail("jo@unal.edu.co")
    	e3.setGrado(10)
    	self._empleados.append(e3)

    	e4 = IngenieroTecnico()
    	e4.setIdent(4)
    	e4.setNombre("Carlos")
    	e4.setApellido("Tamayo")
    	e4.setNumElementPres(0)
    	e4.setRoll(Empleado().tiposEmpleado['3'])
    	e4.setEmail("jtam@metalmecanica.com")
    	e4.setArea("Produccion")
    	self._empleados.append(e4)

    	e5 = Operario()
    	e5.setIdent(5)
    	e5.setNombre("Luis")
    	e5.setApellido("Ospina")
    	e5.setNumElementPres(0)
    	e5.setRoll(Empleado().tiposEmpleado['4'])
    	e5.setEmail("lo@metalmecanica.com")
    	e5.setTipo("Mecanico")
    	self._empleados.append(e5)


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
    			os.system.cls
    			print("%s %s" % (op, "No es una opcion valida"))




if __name__ == "__main__":
	a = Almacen()
	a.menu()
