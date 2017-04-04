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
<<<<<<< HEAD

    def setEstadoActual (self, estadoActual):
        if (estadoActual != Elemento().estados ['1'] and
            estadoActual != Elemento().estados ['2'] and
            estadoActual != Elemento().estados ['3'] ):
            print("\n Estado no reconocido")

        else:
            self._estadoActual = estadoActual
=======
    def setEstadoActual (self, estadoActual):
        if (estadoActual != Elemento().estados ['1'] or
            estadoActual != Elemento().estados ['2'] or
            estadoActual != Elemento().estados ['3'] or)
            print("Estado no reconocido")
        else
            self._estadoActual = estadoActual

    @staticmethod
    def ElementosDisponibles(listado):
        for e in listado:
            
            if(str(e.getEstadoActual()) == Elemento().estados['1']):
<<<<<<< HEAD
<<<<<<< HEAD
               print(e.getNombre())

    @staticmethod
    def InventarioElementos(listado):
        print("El inventario actual de elementos es: ")
        for e in listado:
            print(e.str_Inventario())
=======
=======
>>>>>>> origin/Version_1_PAblo
               elemdis = [e.getCodigo]
               print(e.str_Inventario())
    @staticmethod
    def ElementosPrestados(listado):
        for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['2']):
               print(e.str_Inventario())
    @staticmethod
    def ReservarElementos(listado):
        print (ElementosDisponibles(listado))
        re = input ("Ingrese codigo del elemento que desea prestar: ")
        for k in elemdis:
            if (re == k):
                print ("Elemento Encotrado con Exito")
                op = input ("Desea Reservar?  (S/N)"  )
                if (op == S):
                    for e in listado:
                        if (re == e.getCodigo):
                            e.setEstadoActual() = Elemento().estado['3']
                            print ("Elemento Reservado con exito")
                            break
                    break
                
            
     @staticmethod
     def ModificarReserva (listado):
         for e in listado:
            if(str(e.getEstadoActual()) == Elemento().estados['3']):
               elemres = [e.getCodigo]
               print(e.str_Inventario())
               
         cr = input ("Ingrese codigo del elemento al cual desea modificar la reserva: ")
         for k in elemdis:
            if (cr == k):
                print ("Elemento Encotrado con Exito")
                op = input ("Desea Cancelar Reservar?  (S/N)"  )
                if (op == S):
                    for e in listado:
                        if (re == e.getCodigo):
                            e.setEstadoActual() = Elemento().estado['1']
                            print ("Reserva cancelada  con exito")
                            break
                    break       
<<<<<<< HEAD
         
        
>>>>>>> origin/Version_1_PAblo

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
        
=======
>>>>>>> origin/Version_1_PAblo
    
>>>>>>> refs/remotes/origin/Version_1

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
    def prestarElementos(listado, e): # Agregado por Camilo (El metodo recibe la BD de elementos y un empleado)
        seguirPres = True
        while seguirPres == True:
            if (isinstance(e, Administrativo) and e.getNumRestriccion() < Administrativo.MAX_AD and seguirPres == True) or (isinstance(e, IngenieroTecnico) and e.getNumRestriccion() < IngenieroTecnico.MAX_IT and seguirPres == True) or (isinstance(e, Operario) and e.getNumRestriccion() < Operario.MAX_OP and seguirPres == True):

                cod = int(input("\n Ingrese el codigo del elemento a prestar: "))
                element = Elemento().buscarElementoPorId(listado, cod)

                if element != None and element.getEstadoActual() == Elemento().estados['1']:
                    e.getElementos().append(element) # Cambie e._elementos por e.getElementos()
                    e.setContador(e.getContador() + 1) # El numero de elementos que ha prestado en la historia ya sea que los haya devuelto o no
                    e.setNumElementPres(e.getNumElementPres() + 1) # Lo tiene actualmente prestado
                    e.setNumRestriccion(e.getNumRestriccion() + 1) # Lo que tiene entre prestados y reservados
                    element.setContador(element.getContador() + 1)
                    element.setEstadoActual(Elemento().estados['2']) #El elemento queda marcado como prestado
                    element.setFechaPrestamo(datetime.now())
                    HistorialPrestamo().agregarAHistorial(e, element)
                    op = input("\n Desea Prestar mas Elementos? (S/N): ")
                    if(op == "S"):
                        if(isinstance(e, Administrativo) and e.getNumRestriccion() < Administrativo.MAX_AD) or (isinstance(e, IngenieroTecnico) and e.getNumRestriccion() < IngenieroTecnico.MAX_IT) or (isinstance(e, Operario) and e.getNumRestriccion() < Operario.MAX_OP):
                            seguirPres = True
                        else:
                            print("\n Este Usuario ya No Puede Prestar mas Elementos.")
                            seguirPres = False
                    elif op == "N":
                        seguirPres = False
                    else:
                        print("\n Opcion Invalida")
                elif element != None and element.getEstadoActual() == Elemento().estados['2']:
                    print("\n Lo Sentimos el elemento se encuentra perestado")
                elif element != None and element.getEstadoActual() == Elemento().estados['3']:
                    print("\n Lo Sentimos el Elemento se Encuentra Reservado")
                else:
                    print("\n El código NO se Encuentra Registrado en la BD")
            else:
                print("\n El Empleado ya no Puede Prestar mas Elementos")
                seguirPres = False


    @staticmethod
    def recibirElementos(emp):
        seguirEntregando = True
        Elemento().elementosPrestados(emp.getElementos())
        while(seguirEntregando == True): 
            if emp.getNumElementPres() > 0:
                cod = int(input("\n Ingrese el codigo del elementos que va a entregar: "))
                element = Elemento().buscarElementoPorId(emp.getElementos(), cod)
                if element != None:
                    element.setEstadoActual(Elemento().estados['1'])
                    emp.setNumElementPres(emp.getNumElementPres() - 1)
                    emp.setNumRestriccion(emp.getNumRestriccion() - 1)
                    HistorialPrestamo().agregarFechaEntrega(emp, element)
                    element.setFechaPrestamo(None)
                    emp.getElementos().remove(element)
                    op = input("\n Desea seguir entregando? (S/N): ")
                    if op == "S":
                        seguirEntregando = True
                    elif op == "N":
                        seguirEntregando = False
                    else:
                        print("\n Opcion Invalida")
                else:
                    print("\n Codigo no encontrado en sus elementos prestados.")
            else:
                print("\n El usuario no tiene elementos prestados.")
                seguirEntregando = False

    @staticmethod
    def asentarReserva(listElementEmp, emp): # Recibe un parametro mas emp
        for element in listElementEmp:
            if(element.getEstadoActual() == Elemento().estados['3']):
                element.setEstadoActual(Elemento().estados['2'])
                element.setContador(element.getContador() + 1)
                element.setFechaPrestamo(datetime.now())
                emp.setNumElementPres(emp.getNumElementPres() + 1) # Es emp en vez de element
                emp.setContador(emp.getContador() + 1)
                HistorialPrestamo().agregarAHistorial(emp, element)


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
    def registrarElemento(self):
        elemento = Elemento()
       
        elemento.setCodigo(int(input("\nIngrese codigo del elemento:")))
        elemento.setNombre(str(input("Ingrese nombre del elemento:")))
        elemento.setUbicacion(str(input("Ingrese la ubicacion del elemento:")))
        elemento.setValor(int(input("Ingrese valor economico del elemento:")))
        elemento.setEstadoActual(Elemento().estados['1'])
        self._elementos.append(elemento) 


    @staticmethod
    def reservarElementos(listado, emp):
        if ((emp.getNumRestriccion() >= Administrativo.MAX_AD) or (emp.getNumRestriccion() >= IngenieroTecnico.MAX_IT) or (emp.getNumRestriccion() >= Operario.MAX_OP)):
            print("El usuario no esta autorizado para realizar reservas!")
        else:    
            Elemento().elementosDisponibles(listado)
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
                                emp.setNumRestriccion(emp.getNumRestriccion() + 1) # La agrego Camilo, es para que aumente ese contador de restriccion de numero de elementos cuando se reserva
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
                            emp.setNumRestriccion(emp.getNumRestriccion() - 1) # La agrego Camilo para que le reste a la variable que controla la restriccion 
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
    

