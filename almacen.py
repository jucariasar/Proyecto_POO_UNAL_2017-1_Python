from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from historialprestamo import HistorialPrestamo
from bienvenida import Bienvenida
from mensajes import Mensaje
import sys
import time
import os # Linea nueva para probar


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
        os.system("cls")
        while(salir == False):
            
            email = input("\nIngrese su E-mail: ")
            cc = int(input("Ingrese su Documento: "))
            emp = Empleado().buscarEmpleadoPorId(self._empleados, cc)
            if emp != None and emp.getEmail() == email:
                if isinstance(emp,AdministradorAlmacen):
                    salir2 = False
                    while(salir2 == False):
                        os.system("cls")
                        Mensaje.mostrarMensajes('SelectRollAdmin')
                        opt = int(input("\nIngrese su Opcion: "))
                        if opt == 1:
                            self.autenticacionAdministradorAlmacen(emp)
                        elif opt == 2:
                            self.menuEmpleado(emp)
                            salir = True
                            salir2 = True
                        elif opt == 3:
                            salir = True
                            salir2 = True
                        else:
                            Mensaje.mostrarMensajes('optInvalid')
                else: 
                    self.menuEmpleado(emp)
                    op=input("\n Desea salir del sistema? (S/N): ")
                    if op=="S":
                        salir=True
                    elif op=="N":
                        pass
            else:
                os.system("cls")
                Mensaje.mostrarMensajes('emailDocumentInvalid')
     
    def autenticacionAdministradorAlmacen(self, admin):
        os.system("cls")
        Mensaje.mostrarBienvenidaPersonalizada('bienvenida', admin)
        Mensaje.mostrarMensajes('infoAdmin1')
        user = input("Ingrese su Usuario: ")
        paswd = input("Ingrese su Contraseña: ")

        if admin.getUsuario() == user and admin.getPassword() == paswd:
            self.menuAdministradorAlmacen(admin)
        else:
            Mensaje.mostrarMensajes('userPassInvalid')
            input("\n Presion Enter Para Continuar..")


    def menuAdministradorAlmacen(self, admin):
        salir = False
        os.system("cls")
        while(salir == False):
            Mensaje.mostrarMensajes('menuPpalAdmin')
            op = input("\nIngrese su Opcion: ")
            if op == "1":
                self.menu1AdministradorAlmacen()
            elif op == "2":
                self.menu2AdministradorAlmacen()
            elif op == "3":
                self.menu3AdministradorAlmacen()
            elif op == "4":
                salir = True
            else:
                os.system("cls")
                Mensaje.mostrarMensajes('optInvalid')


    def menuEmpleado(self, admin):
        salir = False
        os.system("cls")
        Mensaje.mostrarBienvenidaPersonalizada('bienvenida', admin)
        while salir == False:
            Mensaje.mostrarMensajes('menuEmpleado')

            op = input("\nIngrese su opcion: ")
            if op == "1":
                os.system("cls")
                Elemento().elementosDisponibles(self._elementos)
            elif(op =="2"):
                os.system("cls")
                Elemento().elementosPrestados(admin._elementos)
            elif(op == "3"):
                os.system("cls")
                Elemento().reservarElementos(self._elementos, admin)
            elif(op == "4"):
                os.system("cls")
                Elemento().modificarReserva(admin._elementos, admin)
            elif(op == "5"):
                os.system("cls")
                salir = True
            else:
                os.system("cls")
                Mensaje.mostrarMensajes('optInvalid')
            

    def menu1AdministradorAlmacen(self):
        salir = False
        os.system("cls")
        while(salir == False):
            Mensaje.mostrarMensajes('menu1Admin')
            op = int(input("\nIngrese su opcion: "))
        
            if(op == 1):
                os.system("cls")
                Elemento().inventarioElementos(self._elementos)
            elif(op == 2):
                os.system("cls")
                Empleado().listadoEmpleados(self._empleados)
            elif(op == 3):
                os.system("cls")
                Elemento().masPrestado(self._elementos)
            elif(op == 4):
                os.system("cls")
                Elemento().cincoMasPrestados(self._elementos)
            elif(op == 5):
                os.system("cls")
                Empleado().masElemPrestados(self._empleados)
            elif(op == 6):
                os.system("cls")
                Empleado().masValorPrestado(self._empleados)
            elif(op == 7):
                os.system("cls")
                Empleado().masHaPrestado(self._empleados)
            elif(op == 8):
                os.system("cls")
                Empleado().rollEstrella(self._empleados)
            elif(op == 9):
                os.system("cls")
                salir = True
            else:
                os.system("cls")
                Mensaje.mostrarMensajes('optInvalid')


    def menu2AdministradorAlmacen(self):
        salir = False
        while salir == False :

            Mensaje.mostrarMensajes('menu2Admin')
            op = input("\nIngrese su opcion: ")
            if op == "1":
                os.system("cls")
                self.menuRegistrarEmpleado()
            elif op == "2":
                os.system("cls")
                Elemento().registrarElemento(self)
        
            elif op == "3":
                    os.system("cls")
                    salir = False
                    while salir == False:    
                   
                        i = int(input("Ingrese la identificacion del Usuario: "))
                        
                        emp = Empleado().buscarEmpleadoPorId(self._empleados, i) 
                   
                        if emp != None:
                            if (Elemento().verificarPrestamo(emp.getElementos())):
                                Mensaje.mostrarMensajes('empNoPuedeSerEliminado1')
                                
                            elif(Elemento().verificarReserva(emp.getElementos())):
                                Mensaje.mostrarMensajes('eliminacionEmp1')
                                Elemento().cancelarReserva(emp.getElementos())
                                Mensaje.mostrarMensajes('eliminacionEmpOk')
                                self._empleados.remove(emp)
                            else:
                                Mensaje.mostrarMensajes('eliminacionEmpOk')
                                self._empleados.remove(emp)
                        else:
                            Mensaje.mostrarMensajes('empNoRegistrado')
                        respuesta = input("\n¿Desea eliminar otro empleado?(s/n):  ") 
                        if(respuesta == 'n') :
                          salir = True    
           

            elif op == "4":        
                    os.system("cls")
                    salir = False
                    while salir == False:   
                        i = int(input("Ingrese el codigo  del elemento: "))
                        elm = Elemento().buscarElementoPorId(self._elementos, i)
                        
                        if elm != None:
                            if (Elemento().verificarPrestamo(self._elementos)):
                                Mensaje.mostrarMensajes('elementNoPuedeSerEliminado1')
                            elif(Elemento().verificarReserva(self._elementos)):
                                Mensaje.mostrarMensajes('eliminacionElement1')
                                Elemento().cancelarReserva(self._elementos)
                                Mensaje.mostrarMensajes('eliminacionElementOk')
                                self._elementos.remove(elm)
                            else:
                                Mensaje.mostrarMensajes('eliminacionElementOk')
                                self._elementos.remove(elm)
                        else:
                            Mensaje.mostrarMensajes('elementNoRegistr')
                        respuesta = input("\n¿Desea eliminar otro elemento?(s/n):  ") 
                        if(respuesta == 'n') :
                          salir = True 

            elif op == "5":
                salir = True
            else:
                Mensaje.mostrarMensajes('optInvalid')                                           


    def menuRegistrarEmpleado(self):
        salir = False
        while salir == False:

                    Mensaje.mostrarMensajes('registEmp1')
                    op = input("\nIngrese su opcion: ")
                    if op == '1':
                       AdministradorAlmacen().registrarEmpleado(self._empleados)
                    elif op == '2' :
                        Operario().registrarEmpleado(self._empleados)
                    elif op == '3' :
                        IngenieroTecnico().registrarEmpleado(self._empleados)
                    elif op == '4' :
                        salir = True
                        break
                    else:
                        Mensaje.mostrarMensajes('optInvalid')

                    Mensaje.mostrarMensajes('registroEmpOk')
                    respuesta = input("\n¿Desea registrar otro empleado?(s/n):  ") 
                    if(respuesta == 'n') :
                       salir = True


    def menu3AdministradorAlmacen(self):
        salir = False
        os.system("cls")
        while salir == False:

            Mensaje.mostrarMensajes('menu3Admin')
            op = input("\nIngrese su opcion: ")

            if op == "1":
                os.system("cls")
                if Elemento().verificarDisponibles(self._elementos): # Linea nueva
                    Elemento().elementosDisponibles(self._elementos)
                    i = int(input("\n Ingrese la identificacion del Usuario: "))
                    emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                    if emp != None:
                        if (Elemento().verificarReserva(emp.getElementos())):
                            Mensaje.mostrarMensajes('menu3Opt1')
                            op2 = input("\n Escoja su opcion: ")
                            salir2 = False
                            while salir2 == False:
                                if op2 == "1":
                                    Elemento().asentarReserva(emp.getElementos(), emp)
                                    os.system("cls")
                                    Mensaje.mostrarMensajes('reserv1Ok')
                                    salir2 = True
                                elif op2 == "2":
                                    Elemento().prestarElementos(self._elementos, emp)
                                    salir2 = True
                                elif op2 == "3":
                                    os.system("cls")
                                    salir2 = True
                                else:
                                    os.system("cls")
                                    Mensaje.mostrarMensajes('optInvalid')
                        else:
                            Elemento().prestarElementos(self._elementos, emp)
                    else:
                        os.system("cls")
                        Mensaje.mostrarMensajes('empNoRegistrado')
                else:
                    Mensaje.mostrarMensajes('elementNoDisponInventario')
                    
            elif op == "2":
                os.system("cls")
                i = int(input("\n Ingrese la identificacion del Usuario: "))
                emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                if emp != None:
                    os.system("cls")
                    if Elemento.verificarPrestamo(emp.getElementos()): ## OJO ACA
                        Elemento().recibirElementos(emp)
                    else:
                        Mensaje.mostrarMensajes('noElementPrest')
                else:
                    os.system("cls")
                    Mensaje.mostrarMensajes('empNoRegistrado')
            elif op == "3":
                if len(HistorialPrestamo().historial) > 0:
                    os.system("cls")
                    Mensaje.mostrarMensajes('impHistorial1')
                    HistorialPrestamo().mostrarHistorial()
                else:
                    os.system("cls")
                    Mensaje.mostrarMensajes('hoHayHistorial')
            elif op == "4":
                os.system("cls")
                salir = True
            else:
                os.system("cls")
                Mensaje.mostrarMensajes('optInvalid')
        

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
       
        os.system("cls")
        Mensaje.mostrarMensajes('LecturaDatosExitosa1')
    
    def crearDatosFicticiosDeUntxt(self):
        Archivo = open("empleados.txt", "r")
        lineas = Archivo.readlines()
        for i in lineas:
            tmp = i.strip('\n').split(';')
            e = Elemento()
            e = Elemento()
            e.setCodigo(int(tmp[0]))
            e.setNombre(tmp[1])
            e.setUbicacion(tmp[2])
            e.setFechaPrestamo(None)
            e.setValor(int(tmp[3]))
            e.setEstadoActual(Elemento().estados['1'])
            self._elementos.append(e)
               
        Archivo.close()


    def salir(self):
        Bienvenida().imprimirDespedida()
        input("\n\n Presione Enter Para Finalizar...")
        sys.exit(0)



    # Primer menu
    def menu(self):
        break_while = 1
        while break_while == 1:

            Mensaje.mostrarMensajes('menuPpal')
            op = input("\nIngrese su Opcion: ")
            accion = self._seleccion.get(op)
            if(accion):
                accion()
            else:
                Mensaje.mostrarMensajes('optInvalid')


if __name__ == "__main__":
    a = Almacen()
    #Bienvenida().imprimirBienvenida()
    #Bienvenida().imprimirBienvenida2()
    #Bienvenida().imprimirBienvenida3()
    Bienvenida().imprimirBienvenida4()
    a.menu()