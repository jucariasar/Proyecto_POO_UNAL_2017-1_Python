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
        "2":self.crearDatosFicticiosDeUntxt,
        "3":self.ingresarAlSistema,
        "4":self.salir
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
                        print("3. Desea volver al menu principal.")
                        opt = int(input("\nIngrese su Opcion: "))
                        if opt == 1:
                            self.autenticacionAdministradorAlmacen(emp)
                            #salir = True
                            #salir2 = True
                        elif opt == 2:
                            self.menuEmpleado(emp)
                            salir = True
                            salir2 = True
                        elif opt == 3:
                            salir = True
                            salir2 = True
                        else:
                            print("\n%d %s" % (opt, "No es una opcion Valida"))
                else: 
                    self.menuEmpleado(emp)
                    op=input("\n Desea salir del sistema? (S/N): ")
                    if op=="S":
                        salir=True
                    elif op=="N":
                        pass
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
            print("4. Cerrar Sesion de Administrador.") # Falta programar estas funcionalidad bien
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
<<<<<<< HEAD
        salir = False
        while salir == False:
            print("\nBienvenido %s %s\n" % (admin.getNombre(), admin.getApellido()))
            print("¿Que desea hacer?\n")
            print("1. Consultar Elementos Disponibles.")
            print("2. Consultar Elementos Prestados.")
            print("3. Reservar Elementos para Prestar.")
            print("4. Modificar Reserva de Elementos.")
            print("5. Cerrar Sesion de Usuario.")

            op = input("\nIngrese su opcion: ")
            if op == "1":
                Elemento().elementosDisponibles(self._elementos)
            elif(op =="2"):
                Elemento().elementosPrestados(admin._elementos)
            elif(op == "3"):
                Elemento().reservarElementos(self._elementos, admin)
            elif(op == "4"):
                Elemento().modificarReserva(admin._elementos, admin)
            elif(op == "5"):
                salir = True
            else:
                print("Opcion erronea")
            

=======
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
        elif(op == 2):
            Elemento().ElementosPrestados(self._elementos)
        elif(op == 3):
            Elemento().ReservarElementos(self._elementos)
        elif(op == 4):
            pass
        elif(op == 5):
            pass
        else(op == 6):
            pass
>>>>>>> refs/remotes/origin/Version_1

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
            op = int(input("\nIngrese su opcion: "+'\n'))
        
            if(op == 1):
<<<<<<< HEAD
                Elemento().inventarioElementos(self._elementos)
            elif(op == 2):
                Empleado().listadoEmpleados(self._empleados) # Para Empleado
            elif(op == 3):
                Elemento().masPrestado(self._elementos)
            elif(op == 4):
                Elemento().cincoMasPrestados(self._elementos)
=======
                Elemento().InventarioElementos(self._elementos)
            elif(op == 2):
                Empleado().ListadoEmpleados(self._empleados)
            elif(op == 3):
                Elemento().MasPrestado(self._elementos)
            elif(op == 4):
                Elemento().CincoMasPrestados(self._elementos)
>>>>>>> refs/remotes/origin/Version_1
            elif(op == 5):
                Empleado().masElemPrestados(self._empleados) # Para Empleado
            elif(op == 6):
                Empleado().masValorPrestado(self._empleados) # Para Empleado
            elif(op == 7):
                Empleado().masHaPrestado(self._empleados) # Para Empleado
            elif(op == 8):
                Empleado().rollEstrella(self._empleados) # Para Empleado
            elif(op == 9):
                salir = True
            else:
                print("\n%s %s" % (op, "No es una opcio valida"))


    def menu2AdministradorAlmacen(self):
        salir = False
        while salir == False :

            print("\n¿Que desea hacer?\n")
            print("1. Registrar Empleado.")
            print("2. Registrar Elemento.")
            print("3. Eliminar Empleado.")
            print("4. Eliminar Elemento.")
            print("5. Volver al Menu Anterior.")
            op = input("\nIngrese su opcion: ")
            # Resta implementar las funcionalidades
            if op == "1":
                   self.menuRegistrarEmpleado()
            elif op == "2":
                   Elemento().registrarElemento(self)
        
            elif op == "3":
                    i = int(input("Ingrese la identificacion del Usuario: "))
                    emp = Empleado().buscarEmpleadoPorId(self._empleados, i) 
           
                    if emp != None:
                        if (Elemento().verificarPrestamo(emp.getElementos())):
                          print("El empleado tiene elementos prestados.No puede ser eliminado")
                        elif(Elemento().verificarReserva(emp.getElementos())):
                          print("El empleado tiene elementos reservados.Estos pasaran a estar disponibles")
                          Elemento().cancelarReserva(emp.getElementos())
                          self._empleados.remove(emp)
                        else:
                          self._empleados.remove(emp)
                    else:
                       print("Empleado no registrado en la base de datos") 
            elif op == "4":        
                    i = int(input("Ingrese el codigo  del elemnto: "))
                    elm = Elemento().buscarElementoPorId(self._elementos, i)
                  
                    if elm != None:
                        if (Elemento().verificarPrestamo(self._elementos)):
                           print("El elemento encuentra prestado.No puede ser eliminado")
                        elif(Elemento().verificarReserva(self._elementos)):
                           print("El elemento tiene reservas, al eliminar el elemento estas se anularan")
                           Elemento().cancelarReserva(self._elementos)
                           self._elementos.remove(elm)
                        else:
                           self._elementos.remove(elm)
                    else:
                     print("Elemento no registrado en la base de datos") 

            elif op == "5":
                   salir = True
            else:
                   print("%s %s" % (op, "No es una opcion Valida"))                                           

   


    def menuRegistrarEmpleado(self):
        print("\n¿Qué tipo de empleado desea registrar?\n")
        print("1.Empleado Administrativo.")
        print("2.Empleado Operario.")
        print("3.Ingeniero Tecnico.")
        op = input("\nIngrese su opcion: ")
        if op == '1':
           AdministradorAlmacen().registrarEmpleado(self._empleados)
        elif op == '2' :
            Operario().registrarEmpleado(self._empleados)
        else:
            IngenieroTecnico().registrarEmpleado(self._empleados)


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
                Elemento().elementosDisponibles(self._elementos)
                i = int(input("\n Ingrese la identificacion del Usuario: "))
                emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                if emp != None:
                    if (Elemento().verificarReserva(emp.getElementos())):
                        print("\n El usuario actualmente tiene elemento(s) reservado(s): ")
                        print("\n ¿Que Desea Hacer?:\n")
                        print(" 1. Asentar la reserva.")
                        print(" 2. Prestar nuevos elementos.")
                        print(" 3. Volver.")
                        op2 = input("\n Escoja su opcion: ")
                        salir2 = False
                        while salir2 == False:
                            if op2 == "1":
                                Elemento().asentarReserva(emp.getElementos(), emp)
                                print("\n El elemento Reservado paso a Prestado con Exito")
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
                i = int(input("\n Ingrese la identificacion del Usuario: "))
                emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                if emp != None:
                    Elemento().recibirElementos(emp)
                else:
                    print("\n El usuario no se encuentra registrado")
            elif op == "3":
                if len(HistorialPrestamo().historial) > 0:
                    print("\n\n El Historial de Prestamos es:")
                    HistorialPrestamo().mostrarHistorial()
                else:
                    print("\n Aun no Existe Historial")
            elif op == "4":
                salir = True
            else:
                print(" %s %s" % (op, "No es una opcion Valida"))
        

    def crearDatosFicticios(self):

        # Se crean empleados y elementos para pruebas

        # Se crean empleados con diferentes roles y se agregan a la lista _empleados

        e1 = AdministradorAlmacen()
        e1.setIdent(70900191)
        e1.setNombre("Alejandro")
        e1.setApellido("Arbelaez Montoya")
        e1.setNumElementPres(0)
        e1.setRoll(Empleado().tiposEmpleado['1'])
        e1.setEmail("aarbelaez1@misena.edu.co")
        e1.setGrado(10)
        e1.setUsuario("aarbelaez1")
        e1.setPassword("70900191")
        self._empleados.append(e1)

        e2 = AdministradorAlmacen()
        e2.setIdent(98670551)
        e2.setNombre("Juan Carlos")
        e2.setApellido("Calle Garzon")
        e2.setNumElementPres(0)
        e2.setRoll(Empleado().tiposEmpleado['1'])
        e2.setEmail("jccalle@misena.edu.co")
        e2.setGrado(10)
        e2.setUsuario("jccalle")
        e2.setPassword("98670551")
        self._empleados.append(e2)

        e3 = Administrativo()
        e3.setIdent(43098368)
        e3.setNombre("Liliana Maria")
        e3.setApellido("Carmona Molano")
        e3.setNumElementPres(0)
        e3.setRoll(Empleado().tiposEmpleado['2'])
        e3.setEmail("lmcarmona86@misena.edu.co")
        e3.setGrado(10)
        self._empleados.append(e3)

        e4 = IngenieroTecnico()
        e4.setIdent(75147008)
        e4.setNombre("Carlos Andres")
        e4.setApellido("Correa Diaz")
        e4.setNumElementPres(0)
        e4.setRoll(Empleado().tiposEmpleado['3'])
        e4.setEmail("ccorrea78@misena.edu.co")
        e4.setArea("Produccion")
        self._empleados.append(e4)

        e5 = Operario()
        e5.setIdent(70725726)
        e5.setNombre("Luis Gonzaga")
        e5.setApellido("Ospina Osorio")
        e5.setNumElementPres(0)
        e5.setRoll(Empleado().tiposEmpleado['4'])
        e5.setEmail("lospinaos@misena.edu.co")
        e5.setTipo("Mecanico")
        self._empleados.append(e5)

        


        # Se crean varios elementos y se agregan a la lista _elementos

        elemento1 = Elemento()
        elemento1.setCodigo(2528)
        elemento1.setNombre("Taladro Percutor Bosh")
        elemento1.setUbicacion("A5")
        elemento1.setFechaPrestamo(None)
        elemento1.setValor(355900)
        elemento1.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento1)
        

        elemento2 = Elemento()
        elemento2.setCodigo(3048)
        elemento2.setNombre("Monitor LED Samsung")
        elemento2.setUbicacion("B4")
        elemento2.setFechaPrestamo(None)
        elemento2.setValor(400000)
        elemento2.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento2)
        

        elemento3 = Elemento()
        elemento3.setCodigo(1025)
        elemento3.setNombre("Multimetro Digital Fluke")
        elemento3.setUbicacion("C1")
        elemento3.setFechaPrestamo(None)
        elemento3.setValor(1200000)
        elemento3.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento3)
        elemento3.setContador(3)

        elemento4 = Elemento()
        elemento4.setCodigo(85)
        elemento4.setNombre("Fuente de Voltaje Uni-t")
        elemento4.setUbicacion("C2")
        elemento4.setFechaPrestamo(None)
        elemento4.setValor(535000)
        elemento4.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento4)
        

        elemento5 = Elemento()
        elemento5.setCodigo(26)
        elemento5.setNombre("Mouse")
        elemento5.setUbicacion("M7")
        elemento5.setFechaPrestamo(None)
        elemento5.setValor(251)
        elemento5.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento5)
        

        elemento6 = Elemento()
        elemento6.setCodigo(27)
        elemento6.setNombre("Lapiz")
        elemento6.setUbicacion("T8")
        elemento6.setFechaPrestamo(None)
        elemento6.setValor(250)
        elemento6.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento6)
        

        print ("\nDatos Leidos con Exito !!!")
    
    def crearDatosFicticiosDeUntxt(self):
        pass


    def salir(self):
        print("\nMuchas gracias por utilizar la aplicacion")
        sys.exit(0)



    # Primer menu
    def menu(self):
        break_while = 1
        while break_while == 1:

            print("")
            print("1. Crear Datos Ficticios.")
            print("2. Crear Datos Ficticios Desde un txt.")
            print("3. Ingresar al sistema.")
            print("4. Salir.")
            op = input("\nIngrese su Opcion: ")
            accion = self._seleccion.get(op)
            if(accion):
                accion()
            else:
                print("%s %s" % (op, "No es una opcion valida"))


if __name__ == "__main__":
    a = Almacen()
    a.menu()
