#Desarrollo Pablo 
from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from historialprestamo import HistorialPrestamo
from mensajes import Mensaje
from datetime import datetime, date, time, timedelta
import calendar
#import os

class Elemento:
    estados = {'1':'Disponible',      
    '2':'Prestado','3':'Reservado'}  

    def __init__(self, codigo=0, descripcion="", modelo="", marca="", ubicacion="", fechaPrestamo=None, valor=0, estadoActual=""):
        self._codigo = codigo
        self._descripcion = descripcion
        self._modelo = modelo
        self._marca = marca
        self._ubicacion = ubicacion
        self._fechaPrestamo = fechaPrestamo
        self._contador = 0
        self._valor = valor
        self._estadoActual = estadoActual 

    def getCodigo (self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getDescripcion (self):
        return self._descripcion

    def setDescripcion (self, descripcion):
        self._descripcion = descripcion

    def getModelo(self):
        return self._modelo

    def setModelo(self, modelo):
        self._modelo = modelo

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getUbicacion (self):
        return self._ubicacion

    def setUbicacion (self, ubicacion):
        self._ubicacion = ubicacion

    def getFechaPrestamo (self):
        return self._fechaPrestamo

    def setFechaPrestamo (self, fechaPrestamo):
        self._fechaPrestamo = fechaPrestamo

    def getContador (self):
        return self._contador

    def setContador (self, contador):
        self._contador = contador

    def getValor (self):
        return self._valor

    def setValor (self, valor):
        self._valor = valor

    def getEstadoActual (self):
        return self._estadoActual

    def setEstadoActual (self, estadoActual):
        if (estadoActual != Elemento().estados ['1'] and
            estadoActual != Elemento().estados ['2'] and
            estadoActual != Elemento().estados ['3'] ):
            Mensaje.mostrarMensajes('estadoNoReconocido')
        else:
            self._estadoActual = estadoActual

    def __str__(self):
        return ("Codigo del Elemento: " + str(self.getCodigo()) + 
            "\n Nombre del Elemento: " + self.getDescripcion() + "\n La ubicacion del Elemento es:  " + self.getUbicacion() +
            "\n Fecha de prestamo: " + self.getFechaPrestamo() +  "\n Cantidad de veces prestado: " + str(self.getContador()) + 
            "\n Estado del Elemento: " + self.getEstadoActual())

    
    def str_Inventario(self):
        return ("\n Código del Elemento: " + str(self.getCodigo()) + "\n Descripción: " + 
            str(self.getDescripcion()) + "\n Marca: " + str(self.getMarca()) + 
            " \n Modelo: " + str(self.getModelo()) + "\n La ubicacion del Elemento es:  " + str(self.getUbicacion()) + 
            "\n Estado del Elemento: " + str(self.getEstadoActual())+'\n')



    @staticmethod
    def verificarReserva(listado): 
        for element in listado:
            if(element.getEstadoActual() == Elemento().estados['3']):
                return True
        return False

    @staticmethod
    def cancelarReserva(listado):
        for element in listado:
            if(element.getEstadoActual() == Elemento().estados['3']):
              element.setEstadoActual(Elemento().estados['1'])



    @staticmethod
    def verificarPrestamo(listado):
        for element in listado:
            if(element.getEstadoActual() == Elemento().estados['2']):
                return True
        return False
    

    @staticmethod
    def prestarElementos(listado, e):
        seguirPres = True
        while seguirPres == True:
            if Elemento().verificarDisponibles(listado):

                if (isinstance(e, Administrativo) and e.getNumRestriccion() < Administrativo.MAX_AD and seguirPres == True) or (isinstance(e, IngenieroTecnico) and e.getNumRestriccion() < IngenieroTecnico.MAX_IT and seguirPres == True) or (isinstance(e, Operario) and e.getNumRestriccion() < Operario.MAX_OP and seguirPres == True):
                    cod = int(input(Mensaje.obtenerMensaje('codElementAPrestar')))
                    element = Elemento().buscarElementoPorId(listado, cod)

                    if element != None and element.getEstadoActual() == Elemento().estados['1']:
                        e.getElementos().append(element)
                        e.setContador(e.getContador() + 1) 
                        e.setNumElementPres(e.getNumElementPres() + 1) 
                        e.setNumRestriccion(e.getNumRestriccion() + 1) 
                        element.setContador(element.getContador() + 1)
                        element.setEstadoActual(Elemento().estados['2'])
                        element.setFechaPrestamo(datetime.now())
                        HistorialPrestamo().agregarAHistorial(e, element)
                        op = input(Mensaje.obtenerMensaje('presMasElementSoN'))
                        if(op == "S"):
                            if(isinstance(e, Administrativo) and e.getNumRestriccion() < Administrativo.MAX_AD) or (isinstance(e, IngenieroTecnico) and e.getNumRestriccion() < IngenieroTecnico.MAX_IT) or (isinstance(e, Operario) and e.getNumRestriccion() < Operario.MAX_OP):
                                if Elemento().verificarDisponibles(listado):
                                    seguirPres = True
                                else:
                                    os.system("cls")
                                    Mensaje.mostrarMensajes('elementNoDisponInventario')
                                    seguirPres = False
                            else:
                                os.system("cls")
                                Mensaje.mostrarMensajes('userFullElement')
                                seguirPres = False
                        elif op == "N":
                            os.system("cls")
                            seguirPres = False
                        else:
                            Mensaje.mostrarMensajes('optInvalid')
                    elif element != None and element.getEstadoActual() == Elemento().estados['2']:
                        Mensaje.mostrarMensajes('estElementPrest')
                    elif element != None and element.getEstadoActual() == Elemento().estados['3']:
                        Mensaje.mostrarMensajes('estElementReserv')
                    else:
                        Mensaje.mostrarMensajes('elementNoRegistr')
                else:
                    Mensaje.mostrarMensajes('userFullElement')
                    seguirPres = False
            else:
                seguirPres = False
                os.system("cls")
                Mensaje.mostrarMensajes('elementNoDisponInventario')


    @staticmethod
    def recibirElementos(emp):
        seguirEntregando = True
        Elemento().elementosPrestados(emp.getElementos())
        while(seguirEntregando == True): 
            if emp.getNumElementPres() > 0:
                cod = int(input(Mensaje.obtenerMensaje('codElementAEntre')))
                element = Elemento().buscarElementoPorId(emp.getElementos(), cod)
                if element != None:
                    element.setEstadoActual(Elemento().estados['1'])
                    emp.setNumElementPres(emp.getNumElementPres() - 1)
                    emp.setNumRestriccion(emp.getNumRestriccion() - 1)
                    HistorialPrestamo().agregarFechaEntrega(emp, element)
                    element.setFechaPrestamo(None)
                    emp.getElementos().remove(element)
                    op = input(Mensaje.obtenerMensaje('entreMasElementosSoN'))
                    if op == "S":
                        seguirEntregando = True
                    elif op == "N":
                        os.system("cls")
                        seguirEntregando = False
                    else:
                        Mensaje.mostrarMensajes('optInvalid')
                else:
                    Mensaje.mostrarMensajes('codNoEncotr')
            else:
                Mensaje.mostrarMensajes('noElementPrest')
                seguirEntregando = False


    @staticmethod
    def asentarReserva(listElementEmp, emp):
        for element in listElementEmp:
            if(element.getEstadoActual() == Elemento().estados['3']):
                element.setEstadoActual(Elemento().estados['2'])
                element.setContador(element.getContador() + 1)
                element.setFechaPrestamo(datetime.now())
                emp.setNumElementPres(emp.getNumElementPres() + 1)
                emp.setContador(emp.getContador() + 1)
                HistorialPrestamo().agregarAHistorial(emp, element)


    @staticmethod
    def buscarElementoPorId(listado, cod):
        for element in listado:
            if element.getCodigo() == cod:
                return element
        return None


    @staticmethod
    def verificarDisponibles(listado): 
        for element in listado:
            if element.getEstadoActual() == Elemento().estados['1']:
                return True
        return False
    
    
    @staticmethod
    def elementosDisponibles(listado):
        Mensaje.mostrarMensajes('elementDisp')
        for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['1']):
                print(e.str_Inventario())


    @staticmethod
    def inventarioElementos(listado):
        print()
        Mensaje.mostrarMensajes('inventElement')
        for e in listado:
            print(e.str_Inventario())

    @staticmethod
    def elementosPrestados(listado):
        Mensaje.mostrarMensajes('elementPrest')
        c = 0
        for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['2']):
                print(e.str_Inventario())
                c = c + 1
        if (c == 0):
            Mensaje.mostrarMensajes('noElementPres2')
    

    @staticmethod
    def registrarElemento(self):
            salir = False
            while salir == False : 
                elemento = Elemento()
                
                elemento.setCodigo(int(input(Mensaje.obtenerMensaje('codElementRegist'))))
                while Elemento().buscarElementoPorId(self._elementos, elemento.getCodigo()) != None:
                    Mensaje.mostrarMensajes('elementYaExite')
                    elemento.setCodigo(int(input(Mensaje.obtenerMensaje('codElementRegist'))))
                
                elemento.setDescripcion(str(input(Mensaje.obtenerMensaje('setNomElement'))))
                elemento.setUbicacion(str(input(Mensaje.obtenerMensaje('setUbiElement'))))
                elemento.setValor(int(input(Mensaje.obtenerMensaje('setValorElement'))))
                elemento.setEstadoActual(Elemento().estados['1'])
                self._elementos.append(elemento)
                Mensaje.mostrarMensajes('elementRegistOk')
                respuesta = input(Mensaje.obtenerMensaje('seguirRegistElement')) 
                if(respuesta == 'n') :
                    salir = True


    @staticmethod
    def reservarElementos(listado, emp):
        if (isinstance(emp, Administrativo) and emp.getNumRestriccion() >= Administrativo.MAX_AD) or (isinstance(emp, IngenieroTecnico) and emp.getNumRestriccion() >= IngenieroTecnico.MAX_IT) or (isinstance(emp, Operario) and emp.getNumRestriccion() >= Operario.MAX_OP):
            Mensaje.mostrarMensajes('userNoAutoriz')
        else:    
            Elemento().elementosDisponibles(listado)
            re = int(input (Mensaje.obtenerMensaje('elementAReserv')))
            elemdis=[]
            for e in listado:
                elemdis.append(e.getCodigo())
            E=False   
            for k in elemdis:
                if (k==re):
                    Mensaje.mostrarMensajes('elementEncontradoOk')
                    op = str(input (Mensaje.obtenerMensaje('reservarSoN')))
                    if (op == "S"):
                        for e in listado:
                            if (re == e.getCodigo()):
                                e.setEstadoActual(Elemento().estados['3']) 
                                emp.setaddElemento(e)
                                emp.setNumRestriccion(emp.getNumRestriccion() + 1) # La agrego Camilo, es para que aumente ese contador de restriccion de numero de elementos cuando se reserva
                                Mensaje.mostrarMensajes('elementReservadoOk')
                                E=True
                                break
                    elif(op=="N"):
                        print("\n Ok")
            
                    else:
                        Mensaje.mostrarMensajes('optInvalid')
            if(E==False):
                Mensaje.mostrarMensajes('elementNoEncontrado')  
            

    @staticmethod
    def modificarReserva(listado, emp):
        E = False
        elemres=[]
        Mensaje.mostrarMensajes('listElementReserv')
        for e in listado:
            if(e.getEstadoActual() == Elemento().estados['3']):
                elemres.append(e.getCodigo())
                print(e.str_Inventario())
               
        cr = int(input (Mensaje.obtenerMensaje('codModReserv')))
        for k in elemres:
            if (cr == k):
                Mensaje.mostrarMensajes('elementEncontradoOk')
                op = input (Mensaje.obtenerMensaje('modReservSoN'))
                if (op == "S"):
                    for e in listado:
                        if (cr == e.getCodigo()):
                            e.setEstadoActual( Elemento().estados['1'])
                            emp.setNumRestriccion(emp.getNumRestriccion() - 1) # La agrego Camilo para que le reste a la variable que controla la restriccion 
                            emp.setdelElemento(e)
                            Mensaje.mostrarMensajes('cancelarReservOk')
                            break

                elif(op=="N"):
                    print("\n Ok")
                    break
                else:
                    Mensaje.mostrarMensajes('optInvalid')
                    break
                E=True
        if(E==False):
            Mensaje.mostrarMensajes('elementNoEncontrado')
             

    @staticmethod
    def masPrestado(listado):
        favorito=0
        elem=""
        for e in listado:
            if (e.getContador()>favorito):
                favorito=e.getContador()
                elem=e
        if(elem!=""):
            Mensaje.mostrarMensajes('elmentMasPrest')
            print ("\n"+str(elem.getDescripcion())+" >> "+"N° veces prestado: "+str(elem.getContador()))
        else:
            Mensaje.mostrarMensajes('ningunElementPrest')


    @staticmethod
    def cincoMasPrestados(listado):
        i=5
        c=0
        lista=[]
        while(i>0 and len(listado)>0):
            favorito=0
            elem=""
            for e in listado:
                if (e.getContador()>favorito):
                    favorito=e.getContador()
                    elem=e
            if(elem!=""):
                lista.append(elem)
                listado.remove(elem)
                c=c+1
            i=i-1
        if (c!=0):
            Mensaje.mostrarMensajes('5MasPrest')
            for j in lista:
                print("\n"+str(j.getDescripcion())+" >> "+"N° veces prestado: "+str(j.getContador()))
        else:
            Mensaje.mostrarMensajes('ningunElementPrest2')
