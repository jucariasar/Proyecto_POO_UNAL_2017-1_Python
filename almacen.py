from empleado import Empleado, system, path
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from historialprestamo import HistorialPrestamo
from bienvenida import Bienvenida
from mensajes import Mensaje
from creardatos import empleadosFicticios, elementosFicticios
from datosaplicacion import guardarDatosEmpleados, guardarDatosElementos, cargarDatosEmpleados, cargarDatosElementos, comprobarArchivo
from sys import exit
from funcionesvalidacion import comprobarCorreoValido
import time
#from os import system, path
#from menusadminalmacen import menu1AdministradorAlmacen

## Comentario para probar
class Almacen:
    salirTotal = False
    def __init__(self):
        self._empleados = [] # Solo utilizado en la creación inicial
        self._elementos = [] # Solo utilizado en la creación inicial
        self._archivoEmpleados = None
        self._archivoElementos = None
        self._seleccion ={
        "1":self.ingresarAlSistema,
        "2":self.consultarInventario,
        "3":self.ingresarSuperUsuario,
        "4":self.salir
        }

    # >>>>>>>  Inicio primera revisión
    def getEmpleados(self):
        return self._empleados


    def setEmpleado(self, empleado):
        self._empleados.append(empleado)


    def getElementos(self):
        return self._elementos


    def setElemento(self, elemento):
        self._elementos.append(elemento)


    def getArchivoEmpleados(self):
        return self._archivoEmpleados


    def setArchivoEmpleados(self, empleado):
        pass


    def getArchivoElementos(self):
        return self._archivoElementos


    def setArchivoElementos(self, elemento):
        pass
    

    def cargarDatosDesdeTexto(self):
        cargarDatosEmpleados(self.getEmpleados())

        
    def gardarDatosEnTexto(self):
        guardarDatosEmpleados(self.getEmpleados())
        guardarDatosElementos(self.getElementos())


    def consultarInventario(self):
        Elemento().inventarioElementos(self.getElementos())
    # >>>>>>>  Final primera revisión.

    def ingresarSuperUsuario(self):
        pass

    # >>>>>>>  Inicio Tercera Revision
    def ingresarAlSistema(self):
        salir = False
        system("cls")
        system("color 0A")
        while(salir == False):
            correo = False
            while correo == False:
                email = input(Mensaje.obtenerMensaje('emailIn'))
                if comprobarCorreoValido(email):
                    correo = True
                    break
                else:
                    system("cls")
                    Mensaje.mostrarMensajes('correoInvalido')
                    Mensaje.mostrarMensajes('intentarNuevo')
            
            cc = int(input(Mensaje.obtenerMensaje('documentIn')))
            emp = Empleado().buscarEmpleadoPorId(self.getEmpleados(), cc)
            if emp != None and emp.getEmail() == email:
                if isinstance(emp, AdministradorAlmacen):
                    salirAdmin = False
                    system("cls")
                    while(salirAdmin == False):
                        Mensaje.mostrarMensajes('SelectRollAdmin')
                        try:
                            opt = int(input(Mensaje.obtenerMensaje('optIn')))
                        except ValueError:
                            system("cls")
                            Mensaje.mostrarMensajes('optInvalid')
                            continue
                        if opt == 1:
                            self.autenticacionAdministradorAlmacen(emp)
                        elif opt == 2:
                            self.menuEmpleado(emp)
                            salir = True
                            salirAdmin = True
                        elif opt == 3:
                            salir = True
                            salirAdmin = True
                            system("cls")
                        else:
                            system("cls")
                            Mensaje.mostrarMensajes('optInvalid')
                else: 
                    self.menuEmpleado(emp)
                    op = input(Mensaje.obtenerMensaje('salirSoN'))
                    if op == "S":
                        salir = True
                    elif op == "N":
                        pass
            else: 
                volverMenu = False
                system("cls")
                while volverMenu == False: 
                    Mensaje.mostrarMensajes('emailDocumentInvalid')
                    Mensaje.mostrarMensajes('volverAnterior')
                    volver = input(Mensaje.obtenerMensaje('optIn'))
                    if volver == 'S' or volver == 's':
                        salir = True
                        break
                    elif volver == 'N' or volver == 'n':
                        volverMenu = True
                        system("cls")
                    else:
                        Mensaje.mostrarMensajes('optInvalid')

    def autenticacionAdministradorAlmacen(self, admin):
        system("cls")
        system("color 0A")
        Mensaje.mostrarBienvenidaPersonalizada('bienvenida', admin)
        Mensaje.mostrarMensajes('infoAdmin1')
        user = input(Mensaje.obtenerMensaje('userIn'))
        paswd = input(Mensaje.obtenerMensaje('passwdIn'))

        if admin.getUsuario() == user and admin.getPassword() == paswd:
            AdministradorAlmacen().menuAdministradorAlmacen(self.getEmpleados(), self.getElementos())
        else:
            Mensaje.mostrarMensajes('userPassInvalid')
            input(Mensaje.obtenerMensaje('continuar'))
    

    def menuEmpleado(self, admin):
        salir = False
        system("cls")
        system("color 0A")
        print()
        Mensaje.mostrarBienvenidaPersonalizada('bienvenida', admin)
        while salir == False:
            print()
            Mensaje.mostrarMensajes('menuEmpleado')

            op = input(Mensaje.obtenerMensaje('optIn'))
            if op == "1":
                system("cls")
                Elemento().elementosDisponibles(self._elementos)
            elif(op =="2"):
                system("cls")
                Elemento().elementosPrestados(admin._elementos)
            elif(op == "3"):
                system("cls")
                Elemento().reservarElementos(self._elementos, admin)
            elif(op == "4"):
                system("cls")
                Elemento().modificarReserva(admin._elementos, admin)
            elif(op == "5"):
                system("cls")
                salir = True
            else:
                system("cls")
                Mensaje.mostrarMensajes('optInvalid')
    # >>>>>>> Final tercera Revision      

    """
    def menu2AdministradorAlmacen(self):
        salir = False
        system("color 0A")
        system("cls")
        while salir == False :

            Mensaje.mostrarMensajes('menu2Admin')
            op = input(Mensaje.obtenerMensaje('optIn'))
            if op == "1":
                system("cls")
                self.menuRegistrarEmpleado()
            elif op == "2":
                system("cls")
                Elemento().registrarElemento(self)
        
            elif op == "3":
                    system("cls")
                    salir = False
                    while salir == False:    
                   
                        i = int(input(Mensaje.obtenerMensaje('idIn')))
                        
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
                        respuesta = input(Mensaje.obtenerMensaje('seguirEliminandoEmp')) 
                        if(respuesta == 'n') :
                          salir = True    
           

            elif op == "4":        
                    system("cls")
                    system("color 0A")
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
                        respuesta = input(Mensaje.obtenerMensaje('seguirEliminandoElement')) 
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
                    op = input(Mensaje.obtenerMensaje('optIn'))
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
                    respuesta = input(Mensaje.obtenerMensaje('seguirRegistEmp')) 
                    if(respuesta == 'n') :
                       salir = True
        """

    def menu3AdministradorAlmacen(self):
        salir = False
        system("cls")
        while salir == False:
            Mensaje.mostrarMensajes('menu3Admin')
            op = input(Mensaje.obtenerMensaje('optIn'))

            if op == "1":
                system("cls")
                i = int(input(Mensaje.obtenerMensaje('idIn')))
                emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                if emp != None:
                    if Elemento().verificarDisponibles(self._elementos) or Elemento().verificarReserva(emp.getElementos()):
                         
                        if (Elemento().verificarReserva(emp.getElementos())):
                            Mensaje.mostrarMensajes('menu3Opt1')
                            op2 = input(Mensaje.obtenerMensaje('optIn'))
                            salir2 = False
                            while salir2 == False:
                                if op2 == "1":
                                    Elemento().asentarReserva(emp.getElementos(), emp)
                                    system("cls")
                                    Mensaje.mostrarMensajes('reserv1Ok')
                                    salir2 = True
                                elif op2 == "2":
                                    Elemento().elementosDisponibles(self._elementos)
                                    Elemento().prestarElementos(self._elementos, emp)
                                    salir2 = True
                                elif op2 == "3":
                                    system("cls")
                                    salir2 = True
                                else:
                                    system("cls")
                                    Mensaje.mostrarMensajes('optInvalid')
                        else:
                            Elemento().elementosDisponibles(self._elementos)
                            Elemento().prestarElementos(self._elementos, emp)
                    else:
                        system("cls")
                        Mensaje.mostrarMensajes('elementNoDisponInventario')    
                else:
                    system("cls")
                    Mensaje.mostrarMensajes('empNoRegistrado')
                    
                    
            elif op == "2":
                system("cls")
                i = int(input(Mensaje.obtenerMensaje('idIn')))
                emp = Empleado().buscarEmpleadoPorId(self._empleados, i)
                if emp != None:
                    system("cls")
                    if Elemento.verificarPrestamo(emp.getElementos()): ## OJO ACA
                        Elemento().recibirElementos(emp)
                    else:
                        Mensaje.mostrarMensajes('noElementPrest')
                else:
                    system("cls")
                    Mensaje.mostrarMensajes('empNoRegistrado')
            elif op == "3":
                if len(HistorialPrestamo().historial) > 0:
                    system("cls")
                    Mensaje.mostrarMensajes('impHistorial1')
                    HistorialPrestamo().mostrarHistorial()
                else:
                    os.system("cls")
                    Mensaje.mostrarMensajes('hoHayHistorial')
            elif op == "4":
                system("cls")
                salir = True
            else:
                system("cls")
                Mensaje.mostrarMensajes('optInvalid')
    

    def salir(self):
        system("color 0A")
        system("cls")
        Bienvenida().imprimirDespedida()
        input(Mensaje.obtenerMensaje('finalizar'))
        exit(0)


    # >>>>>>>  Inicio segunda revisión
    def menu(self):
        break_while = 1
        ejecucionEmp = 0
        ejecucionElem = 0
        while break_while == 1:

            if not comprobarArchivo("Datos", "Empleados.csv"):
                empleadosFicticios(self.getEmpleados())
                guardarDatosEmpleados(self.getEmpleados())
                ejecucionEmp = 1
            elif ejecucionEmp == 0:
                cargarDatosEmpleados(self.getEmpleados())
                ejecucionEmp = 1

            if not comprobarArchivo("Datos", "Elementos.csv"):
                elementosFicticios(self.getElementos())
                guardarDatosElementos(self.getElementos())
                ejecucionElem = 1
            elif ejecucionElem == 0:
                cargarDatosElementos(self.getElementos())
                ejecucionElem = 1
            
            #system("cls")
            print()
            Bienvenida().imprimirBienvenida4()
            Mensaje.mostrarMensajes('menuPpal')
            op = input(Mensaje.obtenerMensaje('optIn'))
            accion = self._seleccion.get(op)
            if(accion):
                accion()
            else:
                Mensaje.mostrarMensajes('optInvalid')
    # >>>>>>>  Final segunda revisión

if __name__ == "__main__":
    a = Almacen()
    #Bienvenida().imprimirBienvenida4()
    a.menu()