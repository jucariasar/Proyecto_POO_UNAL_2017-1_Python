#Desarrollo Pablo 
from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario

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
        self._estadoActual = estadoActual

    @staticmethod
    def ElementosDisponibles(listado):
        for e in listado:
            
            if(str(e.getEstadoActual()) == Elemento().estados['1']):
               print(e.getNombre())

    @staticmethod
    def verificarReserva(listado): # Agregado por Camilo
        for element in listado:
            if(element.getEstadoActual() == Elemento().estados['3']):
                return True

    @staticmethod
    def prestarElementos(listado, e): # Agregado por Camilo (El metodo recibe la BD de elementos y un empleado)
        seguirPres = True
        while seguirPres == True:

            if (isinstance(e, Administrativo) and e.getNumElementPres() <= Administrativo.MAX_AD and seguirPres == True) or (isinstance(e, IngenieroTecnico) and e.getNumElementPres() <= IngenieroTecnico.MAX_It and seguirPres == True) or (isinstance(e, Operario) and e.getNumElementPres() <= Operario.MAX_OP and seguirPres == True):
                cod = int(input("Ingrese el codigo del elemento a prestar: "))
                element = Elemento().buscarElementoPorId(listado, cod)

                if element != None and element.getEstadoActual() == Elemento().estados['1']:
                    e._elementos.append(element)
                    e.setContador(e.getContador() + 1)
                    e.setNumElementPres(e.getNumElementPres() + 1)
                    element.setContador(element.getContador() + 1)
                    #Almacen().agregarHistorial(e, element) Se debe agregar al historial
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
    def buscarElementoPorId(listado, cod):
        for element in listado:
            if element.getCodigo() == cod:
                return element
        return None



    def __str__(self):
        return ("Codigo del Elemento: " + str(self.getCodigo()) + 
            "\n Nombre del Elemento: " + self.getNombre() + "\n La ubicacion del Elemento es:  " + self.getUbicacion() +
            "\n Fecha de prestamo: " + self.getFechaPrestamo() +  "\n Cantidad de veces prestado: " + str(self.getContador()) + 
            "\n Estado del Elemento: " + self.getEstadoActual())
