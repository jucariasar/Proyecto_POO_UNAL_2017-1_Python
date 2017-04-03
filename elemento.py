#Desarrollo Pablo 
from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from historialprestamo import HistorialPrestamo
from datetime import datetime, date, time, timedelta
import calendar

class Elemento:
    estados = {'1':'Disponible',      ## Diccionario estatico para estandarizar los estados
    '2':'Prestado','3':'Reservado'}   ## de los elementos (Camilo Agrego esta linea)

    def __init__(self, codigo=0, nombre="", ubicacion="", fechaPrestamo=None, valor=0, estadoActual=""):
        self._codigo = codigo
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._fechaPrestamo = fechaPrestamo
        self._contador = 0
        self._valor = valor
        self._estadoActual = estadoActual # Los tipos definidos en el diccionario estatico de estados

    def getCodigo (self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getNombre (self):
        return self._nombre

    def setNombre (self, nombre):
        self._nombre = nombre

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
            print("\n Estado no reconocido")

        else:
            self._estadoActual = estadoActual

    def __str__(self):
        return ("Codigo del Elemento: " + str(self.getCodigo()) + 
            "\n Nombre del Elemento: " + self.getNombre() + "\n La ubicacion del Elemento es:  " + self.getUbicacion() +
            "\n Fecha de prestamo: " + self.getFechaPrestamo() +  "\n Cantidad de veces prestado: " + str(self.getContador()) + 
            "\n Estado del Elemento: " + self.getEstadoActual())

    # Método de instancia agregado por Pablo o Jaider
    def str_Inventario(self):
        return ("\n Nombre del Elemento: " + str(self.getNombre())+ "\n Codigo del Elemento: " + 
            str(self.getCodigo())+ "\n La ubicacion del Elemento es:  " + str(self.getUbicacion()) + 
            "\n Estado del Elemento: " + str(self.getEstadoActual())+'\n')



# Inicio de métodos estáticos agregados por Camilo
    @staticmethod
    def verificarReserva(listado): # Agregado por Camilo
        for element in listado:
            if(element.getEstadoActual() == Elemento().estados['3']):
                return True
        return False

    @staticmethod
    def prestarElementos(listado, e): # Agregado por Camilo (El metodo recibe la BD de elementos y un empleado)
        seguirPres = True
        while seguirPres == True:

            if (isinstance(e, Administrativo) and e.getNumElementPres() <= Administrativo.MAX_AD and seguirPres == True) or (isinstance(e, IngenieroTecnico) and e.getNumElementPres() <= IngenieroTecnico.MAX_IT and seguirPres == True) or (isinstance(e, Operario) and e.getNumElementPres() <= Operario.MAX_OP and seguirPres == True):
                cod = int(input("Ingrese el codigo del elemento a prestar: "))
                element = Elemento().buscarElementoPorId(listado, cod)

                if element != None and element.getEstadoActual() == Elemento().estados['1']:
                    e.getElementos().append(element) # Cambie e._elementos por e.getElementos()
                    e.setContador(e.getContador() + 1)
                    e.setNumElementPres(e.getNumElementPres() + 1)
                    element.setContador(element.getContador() + 1)
                    element.setEstadoActual(Elemento().estados['2']) #El elemento queda marcado como prestado
                    element.setFechaPrestamo(datetime.now())
                    HistorialPrestamo().agregarAHistorial(e, element)
                    op = input("Desea prestar mas elementos s/n: ")
                    if(op == "s"):
                        seguirPres = True
                    elif op == "n":
                        seguirPres = False
                    else:
                        print("Opcion Invalida")
                elif element != None and element.getEstadoActual() == Elemento().estados['2']:
                    print("El elemento se encuentra perestado")
                elif element != None and element.getEstadoActual() == Elemento().estados['3']:
                    print("El elementos se encuentra reservado")
                else:
                    print("El código NO se encuentra registrado en la BD")
            else:
                print("El empleado ya no puede prestar mas elementos")
                seguirPres = False


    @staticmethod
    def recibirElementos(emp):
        seguirEntregando = True
        while(seguirEntregando == True): 
            if len(emp.getElementos()) > 0:
                cod = int(input("Ingrese el codigo del elementos que va a entregar: "))
                element = Elemento().buscarElementoPorId(emp.getElementos(), cod)
                if element != None:
                    element.setEstadoActual(Elemento().estados['1'])
                    emp.setNumElementPres(emp.getNumElementPres() - 1)
                    HistorialPrestamo().agregarFechaEntrega(emp, element)
                    element.setFechaPrestamo(None)
                    emp.getElementos().remove(element)
                    op = input("Desea seguir entregando s/n: ")
                    if op == "s":
                        seguirEntregando = True
                    elif op == "n":
                        seguirEntregando = False
                    else:
                        print("Opcion Invalida")
                else:
                    print("Codigo no encontrado en sus elementos prestados.")
            else:
                print("El usuario no tiene elementos prestados.")
                seguirEntregando = False

    @staticmethod
    def asentarReserva(listElementEmp):
        for element in listElementEmp:
            if(element.getEstadoActual() == Elemento().estados['3']):
                element.setEstadoActual(Elemento().estados['2'])
                element.setNumElementPres(getNumElementPres() + 1)
                element.setContador(getContador() + 1)


    @staticmethod
    def buscarElementoPorId(listado, cod):
        for element in listado:
            if element.getCodigo() == cod:
                return element
        return None
    # Fin de métodos estaticos agregados por Camilo



    # Inicio de métodos estáticos agregados por Pablo y Jaider
    @staticmethod
    def elementosDisponibles(listado):
        print("\n Los elemntos disponibles son: ")
        for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['1']):
                print(e.str_Inventario())

    @staticmethod
    def inventarioElementos(listado):
        print("\n El inventario actual de elementos es: ")
        for e in listado:
            print(e.str_Inventario())

    @staticmethod
    def elementosPrestados(listado):
        print ("\n Los elementos prestados son: ")
        c = 0
        for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['2']):
                print(e.str_Inventario())
                c = c + 1
        if (c == 0):
            print("\n No hay elementos prestados")

    @staticmethod
    def reservarElementos(listado, emp):
        Elemento().ElementosDisponibles(listado)
        re = int(input ("\n Ingrese codigo del elemento que desea reservar: "))
        elemdis=[]
        for e in listado:
            elemdis.append(e.getCodigo())
        E=False   
        for k in elemdis:
            if (k==re):
                print ("\n Elemento Encotrado con Exito")
                op = str(input ("\n Desea Reservar?  (S/N): "))
                if (op == "S"):
                    for e in listado:
                        if (re == e.getCodigo()):
                            e.setEstadoActual(Elemento().estados['3']) 
                            emp.setaddElemento(e)
                            print ("\n Elemento Reservado con exito")
                            E=True
                            break
                elif(op=="N"):
                    print("\n Ok")
            
                else:
                    print("\n Opcion erronea")
        if(E==False):
            print("\n Elemento no encontrado")  
            

    @staticmethod
    def modificarReserva(listado, emp):
        E = False
        elemres=[]
        print("\n Sus elementos reservados son: ")
        for e in listado:
            if(e.getEstadoActual() == Elemento().estados['3']):
                elemres.append(e.getCodigo())
                print(e.str_Inventario())
               
        cr = int(input ("\n Ingrese codigo del elemento al cual desea modificar la reserva: "))
        for k in elemres:
            if (cr == k):
                print ("\n Elemento Encotrado con Exito")
                op = input ("\n Desea Cancelar Reservar?  (S/N): "  )
                if (op == "S"):
                    for e in listado:
                        if (cr == e.getCodigo()):
                            e.setEstadoActual( Elemento().estados['1']) 
                            emp.setdelElemento(e)
                            print ("\n Reserva cancelada  con éxito")
                            
                            break

                elif(op=="N"):
                    print("\n Ok")
                    break
                else:
                    print("\n Opción erronea")
                    break
                E=True
        if(E==False):
            print("\n Elemento no encontrado")                   


    @staticmethod
    def masPrestado(listado):
        favorito=0
        elem=""
        for e in listado:
            if (e.getContador()>favorito):
                favorito=e.getContador()
                elem=e
        if(elem!=""):
            print("El elemento mas prestado es: ")
            print ("\n"+str(elem.getNombre())+" >> "+"N° veces prestado: "+str(elem.getContador()))
        else:
            print("\n Ningun elemento ha sido prestado")


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
            print("\n Los 5 elementos mas prestados son: ")
            for j in lista:
                print("\n"+str(j.getNombre())+" >> "+"N° veces prestado: "+str(j.getContador()))
        else:
            print ("\n Aun no hay elemntos prestados")
    

