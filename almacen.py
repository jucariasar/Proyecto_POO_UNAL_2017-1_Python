from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from historialprestamo import HistorialPrestamo
from bienvenida import Bienvenida
from mensajes import Mensaje
from creardatos import empleadosFicticios, elementosFicticios
from datosaplicacion import guardarDatos
import sys
import time
import os

## Comentario para probar
class Almacen:
    salirTotal = False    
    def __init__(self):
        self._empleados = []
        self._elementos = []
        self._seleccion ={
        "1":self.crearDatosFicticios,
        "2":self.cargarDatosDesdeTexto,
        "3":self.gardarDatosEnTexto,
        "4":self.ingresarAlSistema,
        "5":self.salir
        }

    def getEmpleados(self):
        return self._empleados

    def setEmpleado(self, empleado):
        self._empleados.append(empleado)

    def getElementos(self):
        return self._elementos

    def setElemento(self, elemento):
        self._elementos.append(elemento)

    def crearDatosFicticios(self):

        # Se crean empleados y elementos para pruebas

        # Se crean empleados con diferentes roles y se agregan a la lista _empleados
        empleadosFicticios(self.getEmpleados())

        # Se crean varios elementos y se agregan a la lista _elementos
        elementosFicticios(self.getElementos())

       
        os.system("cls")
        os.system("color 0A")
        Mensaje.mostrarMensajes('LecturaDatosExitosa1')

    def cargarDatosDesdeTexto(self):


        """
        Archivo = open("elementos.txt", "r")
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
        Mensaje.mostrarMensajes('LecturaDatosExitosa1')
        Archivo.close()"""
    
    def gardarDatosEnTexto(self):
        #Guarda datos en archivo de texto (csv)
        guardarDatos(self.getEmpleados())
        #Elemento().guardarDatosEntxt(self)

    def ingresarAlSistema(self):
        salir = False
        os.system("cls")
        os.system("color 0A")
        while(salir == False):
            
            email = input(Mensaje.obtenerMensaje('emailIn'))
            cc = int(input(Mensaje.obtenerMensaje('documentIn')))
            emp = Empleado().buscarEmpleadoPorId(self._empleados, cc)
            if emp != None and emp.getEmail() == email:
                if isinstance(emp,AdministradorAlmacen):
                    salir2 = False
                    while(salir2 == False):
                        os.system("cls")
                        Mensaje.mostrarMensajes('SelectRollAdmin')
                        opt = int(input(Mensaje.obtenerMensaje('optIn')))
                        if opt == 1:
                            self.autenticacionAdministradorAlmacen(emp)
                        elif opt == 2:
                            self.menuEmpleado(emp)
                            salir = True
                            salir2 = True
                        elif opt == 3:
                            salir = True
                            salir2 = True
                            os.system("cls")
                        else:
                            Mensaje.mostrarMensajes('optInvalid')
                else: 
                    self.menuEmpleado(emp)
                    op=input(Mensaje.obtenerMensaje('salirSoN'))
                    if op=="S":
                        salir=True
                    elif op=="N":
                        pass
            else:
                os.system("cls")
                Mensaje.mostrarMensajes('emailDocumentInvalid')
     
    def autenticacionAdministradorAlmacen(self, admin):
        os.system("cls")
        os.system("color 0A")
        Mensaje.mostrarBienvenidaPersonalizada('bienvenida', admin)
        Mensaje.mostrarMensajes('infoAdmin1')
        user = input(Mensaje.obtenerMensaje('userIn'))
        paswd = input(Mensaje.obtenerMensaje('passwdIn'))

        if admin.getUsuario() == user and admin.getPassword() == paswd:
            self.menuAdministradorAlmacen(admin)
        else:
            Mensaje.mostrarMensajes('userPassInvalid')
            input(Mensaje.obtenerMensaje('continuar'))


    def menuAdministradorAlmacen(self, admin):
        salir = False
        os.system("cls")
        os.system("color 0A")
        while(salir == False):
            Mensaje.mostrarMensajes('menuPpalAdmin')
            op = input(Mensaje.obtenerMensaje('optIn'))
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
        os.system("color 0A")
        Mensaje.mostrarBienvenidaPersonalizada('bienvenida', admin)
        while salir == False:
            Mensaje.mostrarMensajes('menuEmpleado')

            op = input(Mensaje.obtenerMensaje('optIn'))
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
        os.system("color 0A")
        while(salir == False):
            Mensaje.mostrarMensajes('menu1Admin')
            op = int(input(Mensaje.obtenerMensaje('optIn')))
        
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
        os.system("color 0A")
        os.system("cls")
        while salir == False :

            Mensaje.mostrarMensajes('menu2Admin')
            op = input(Mensaje.obtenerMensaje('optIn'))
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
                    os.system("cls")
                    os.system("color 0A")
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


    def menu3AdministradorAlmacen(self):
        salir = False
        os.system("cls")
        while salir == False:
            Mensaje.mostrarMensajes('menu3Admin')
            op = input(Mensaje.obtenerMensaje('optIn'))

            if op == "1":
                os.system("cls")
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
                                    os.system("cls")
                                    Mensaje.mostrarMensajes('reserv1Ok')
                                    salir2 = True
                                elif op2 == "2":
                                    Elemento().elementosDisponibles(self._elementos)
                                    Elemento().prestarElementos(self._elementos, emp)
                                    salir2 = True
                                elif op2 == "3":
                                    os.system("cls")
                                    salir2 = True
                                else:
                                    os.system("cls")
                                    Mensaje.mostrarMensajes('optInvalid')
                        else:
                            Elemento().elementosDisponibles(self._elementos)
                            Elemento().prestarElementos(self._elementos, emp)
                    else:
                        os.system("cls")
                        Mensaje.mostrarMensajes('elementNoDisponInventario')    
                else:
                    os.system("cls")
                    Mensaje.mostrarMensajes('empNoRegistrado')
                    
                    
            elif op == "2":
                os.system("cls")
                i = int(input(Mensaje.obtenerMensaje('idIn')))
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
    

    def salir(self):
        os.system("color 0A")
        os.system("cls")
        Bienvenida().imprimirDespedida()
        input(Mensaje.obtenerMensaje('finalizar'))
        sys.exit(0)


    # Primer menu
    def menu(self):
        break_while = 1
        while break_while == 1:
            print()
            print()
            Mensaje.mostrarMensajes('menuPpal')
            print()
            op = input(Mensaje.obtenerMensaje('optIn'))
            accion = self._seleccion.get(op)
            if(accion):
                accion()
            else:
                Mensaje.mostrarMensajes('optInvalid')


if __name__ == "__main__":
    a = Almacen()
    Bienvenida().imprimirBienvenida4()
    a.menu()