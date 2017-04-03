#PRUEBA DE POO
from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from historialprestamo import HistorialPrestamo
import sys
import time


class Almacen:
    salirTotal = False    
    def __init__(self):
        self._empleados = []
        self._elementos = []
        #self._historial = [] Se paso como estatico para la clase historial
        self._seleccion ={
        "1":self.crearDatosFicticios,
        "2":self.ingresarAlSistema,
        "3":self.salir
        }


    def ingresarAlSistema(self):
        salir = False
        while(salir == False):

            email = input("\nIngrese su E-mail: ")
            cc = int(input("Ingrese su Documento: "))
            emp = Empleado().buscarEmpleadoPorId(self._empleados, cc)
            if emp != None and emp.getEmail() == email:
                if isinstance(emp,AdministradorAlmacen):
                    salir2 = False
                    while(salir2 == False):
                        print("\nCon que Roll Desea Ingresar:\n")
                        print("1. Como Administrador del Almacen.")
                        print("2. Como Empleado NO Administrador.")
                        opt = int(input("\nIngrese su Opcion: "))
                        if opt == 1:
                            self.autenticacionAdministradorAlmacen(emp)
                            salir = True
                            salir2 = True
                        elif opt == 2:
                            self.menuEmpleado(emp)
                            salir = True
                            salir2 = True
                        else:
                            print("\n%d %s" % (opt, "No es una opcion Valida"))
                else: 
                    self.menuEmpleado(emp)
                    salir = True
            else:
                print("\nE-mail y/o Documento Invalido\n")
                # probando algo con un delay y regerso al menu en caso de error 
            

     
    def autenticacionAdministradorAlmacen(self, admin):
        print("\nBienvenido %s %s\n" % (admin.getNombre(), admin.getApellido()))
        print("A continuacion debe de ingresar su usuario y contraseña para " +
            "ingresar a administrar la aplicacion\n")
        user = input("Ingrese su Usuario: ")
        paswd = input("Ingrese su Contraseña: ")
        if admin.getUsuario() == user and admin.getPassword() == paswd:
            self.menuAdministradorAlmacen(admin)
        else:
            print("Usuario y/o passwor incorrecto.")


    def menuAdministradorAlmacen(self, admin):
        salir = False
        while(salir == False):
            print("\nMenu de Usuario Administrador del Almacen:")
            print("\n1. Ir al Menu de Consultas.")
            print("2. Ir al Menu de Registros / Borrados.")
            print("3. Prestar / Recibir.")
            print("4. Salir.") # Falta programar estas funcionalidad bien
            op = input("\nIngrese su Opcion: ")
            if op == "1":
                self.menu1AdministradorAlmacen()
                #salir = True
            elif op == "2":
                self.menu2AdministradorAlmacen()
                #salir = True
            elif op == "3":
                self.menu3AdministradorAlmacen()
                #salir = True
            elif op == "4":
                salir = True
            else:
                print("%s %s" % (op, "No es una opcion valida"))


    def menuEmpleado(self, admin):
        print("\nBienvenido %s %s\n" % (admin.getNombre(), admin.getApellido()))
        print("¿Que desea hacer?\n")
        print("1. Consultar Elementos Disponibles.")
        print("2. Consultar Elementos Prestados.")
        print("3. Reservar Elementos para Prestar.")
        print("4. Modificar Reserva de Elementos.")
        print("5. Cancelar Reserva de Elementos.")
        print("6. Cerrar Sesion de Usuario.")
        op = input("\nIngrese su opcion: ")
        # Resta implementar las funcionalidades
        if op == "1":
            Elemento().ElementosDisponibles(self._elementos)
            input()


    def menu1AdministradorAlmacen(self):
        salir = False
        while(salir == False):
            print("\n¿Que consulta desea realizar?\n")
            print("1. Consultar Inventario de Elementos.")
            print("2. Consultar Base de Datos de Empleados.")
            print("3. Consultar el Elemento mas Prestado.")
            print("4. Consultar los 5 Elementos mas Prestados.")
            print("5. Consultar Empleado con mas Elementos Prestados.")
            print("6. Consultar Empleados con mas Valor Prestado.")
            print("7. Consultar el Empleado que mas Presta.")
            print("8. Consultar el Roll que mas Presta.")
            print("9. Volver al Menu Anterior.")
            op = int(input("\nIngrese su opcion: "))
        # Resta implementar las funcionalidades

            if(op == 1):
                pass
            elif(op == 2):
                pass
            elif(op == 3):
                pass
            elif(op == 4):
                pass
            elif(op == 5):
                pass
            elif(op == 6):
                pass
            elif(op == 7):
                pass
            elif(op == 8):
                pass
            elif(op == 9):
                salir = True
            else:
                print("\n%s %s" % (op, "No es una opcio valida"))


    def menu2AdministradorAlmacen(self):
        print("\n¿Que desea hacer?\n")
        print("1. Registrar Empleado.")
        print("2. Registrar Elemento.")
        print("3. Eliminar Empleado.")
        print("4. Eliminar Elemento.")
        print("5. Volver al Menu Anterior.")
        op = input("\nIngrese su opcion: ")
        # Resta implementar las funcionalidades


    def menu3AdministradorAlmacen(self):
        salir = False
        while salir == False:

            print("\n¿Que desea hacer?\n")
            print("1. Prestar Elementos.")
            print("2. Recibir Elementos.")
            print("3. Mostrar Historial.")
            print("4. Volver al Menu Anterior.")
            op = input("\nIngrese su opcion: ")

            if op == "1":
                i = int(input("Ingrese la identificacion del Usuario: "))
                emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                if emp != None:
                    if (Elemento().verificarReserva(emp.getElementos())):
                        print("El usuario actualmente tiene elemento(s) reservado(s): ")
                        print("Desea: ")
                        print("1. Asentar la reserva.")
                        print("2. Prestar nuevos elementos.")
                        print("3. Volver.")
                        op2 = input("Escoja su opcion: ")
                        salir2 = True
                        while salir2 == False:
                            if op2 == "1":
                                Elemento().asentarReserva(emp.getElementos())
                                salir2 = True
                            elif op2 == "2":
                                Elemento().prestarElementos(self._elementos, emp)
                                salir2 = True
                            elif op2 == "3":
                                salir2 = True
                            else:
                                print("Opcion no valida.")
                    else:
                        Elemento().prestarElementos(self._elementos, emp)
                else:
                    print("El usuario no se encuentra registrado")

            elif op == "2":
                i = int(input("Ingrese la identificacion del Usuario: "))
                emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                if emp != None:
                    Elemento().recibirElementos(emp)
                else:
                    print("El usuario no se encuentra registrado")
            elif op == "3":
                HistorialPrestamo().mostrarHistorial()
            elif op == "4":
                salir = True
            else:
                print("%s %s" % (op, "No es una opcion Valida"))
        

    def crearDatosFicticios(self):

        # Se crean empleados y elementos para pruebas

        # Se crean empleados con diferentes roles y se agregan a la lista _empleados

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


        # Se crean varios elementos y se agregan a la lista _elementos

        elemento1 = Elemento()
        elemento1.setCodigo(25)
        elemento1.setNombre("Taladro")
        elemento1.setUbicacion("A5")
        elemento1.setFechaPrestamo(None)
        elemento1.setValor(250)
        elemento1.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento1)

        elemento2 = Elemento()
        elemento2.setCodigo(35)
        elemento2.setNombre("Monitor LED")
        elemento2.setUbicacion("B4")
        elemento2.setFechaPrestamo(None)
        elemento2.setValor(125)
        elemento2.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento2)

        elemento3 = Elemento()
        elemento3.setCodigo(45)
        elemento3.setNombre("Multimetro")
        elemento3.setUbicacion("C1")
        elemento3.setFechaPrestamo(None)
        elemento3.setValor(120)
        elemento3.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento3)

        elemento4 = Elemento()
        elemento4.setCodigo(85)
        elemento4.setNombre("Pulidora")
        elemento4.setUbicacion("D5")
        elemento4.setFechaPrestamo(None)
        elemento4.setValor(230)
        elemento4.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento4)

        print ("Datos leidos con exito")


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
    		op = input("\nIngrese su Opcion: ")
    		accion = self._seleccion.get(op)
    		if(accion):
    			accion()
    		else:
    			print("%s %s" % (op, "No es una opcion valida"))


if __name__ == "__main__":
	a = Almacen()
	a.menu()
