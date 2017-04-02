#Desarrollo Pablo 
from empleado import Empleado


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
    def InventarioElementos(listado):
        print("El inventario actual de elementos es: ")
        for e in listado:
            print(e.str_Inventario())

    @staticmethod
    def MasPrestado(listado):
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
            print("Ningun elemento ha sido prestado")
    @staticmethod
    def CincoMasPrestados(listado):
        print("Los 5 elementos mas prestados son: ")
        i=5
        while(i>0):
            favorito=0
            elem=""
            for e in listado:
                if (e.getContador()>favorito):
                    favorito=e.getContador()
                    elem=e
            if(elem!=""):
                print ("\n"+str(elem.getNombre())+" >> "+"N° veces prestado: "+str(elem.getContador()))
                listado.remove(elem)
            else:
                print("Ningun elemento ha sido prestado")
            i=i-1
        
    
    def __str__(self):
        return ("\n Nombre del Elemento: " + str(self.getNombre())+ 
             "\n Codigo del Elemento: " + str(self.getCodigo())+ "\n La ubicacion del Elemento es:  " + str(self.getUbicacion()) +
            "\n Fecha de prestamo: " + str(self.getFechaPrestamo()) +  "\n Cantidad de veces prestado: " + str(self.getContador()) + 
            "\n Estado del Elemento: " + str(self.getEstadoActual()))
    def str_Inventario(self):
        return ("\n Nombre del Elemento: " + str(self.getNombre())+ "\n Codigo del Elemento: " +
         str(self.getCodigo())+ "\n La ubicacion del Elemento es:  " + str(self.getUbicacion()) +
             "\n Estado del Elemento: " + str(self.getEstadoActual()))
