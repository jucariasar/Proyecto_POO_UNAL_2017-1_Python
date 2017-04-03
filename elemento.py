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
        if (estadoActual != Elemento().estados ['1'] and
            estadoActual != Elemento().estados ['2'] and
            estadoActual != Elemento().estados ['3'] ):
            print("\n Estado no reconocido")

        else:
            self._estadoActual = estadoActual

    @staticmethod
    def ElementosDisponibles(listado):
        print("\n Los elemntos disponibles son: ")
        for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['1']):
               print(e.str_Inventario())

    @staticmethod
    def InventarioElementos(listado):
        print("\n El inventario actual de elementos es: ")
        for e in listado:
            print(e.str_Inventario())

    @staticmethod
    def ElementosPrestados(listado):
        print ("\n Los elementos prestados son: ")
        c = 0
        for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['2']):
                print(e.str_Inventario())
                c = c + 1
        if (c == 0):
            print("\n No hay elementos prestados")

    @staticmethod
    def ReservarElementos(listado,emp):
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
    def ModificarReserva (listado,emp):
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
            print("\n Ningun elemento ha sido prestado")
    @staticmethod
    def CincoMasPrestados(listado):
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
    

    def __str__(self):
        return ("Codigo del Elemento: " + str(self.getCodigo()) + 
            "\n Nombre del Elemento: " + self.getNombre() + "\n La ubicacion del Elemento es:  " + self.getUbicacion() +
            "\n Fecha de prestamo: " + self.getFechaPrestamo() +  "\n Cantidad de veces prestado: " + str(self.getContador()) + 
            "\n Estado del Elemento: " + self.getEstadoActual())

    def str_Inventario(self):
        return ("\n Nombre del Elemento: " + str(self.getNombre())+ "\n Codigo del Elemento: " +
         str(self.getCodigo())+ "\n La ubicacion del Elemento es:  " + str(self.getUbicacion()) +
             "\n Estado del Elemento: " + str(self.getEstadoActual())+'\n')