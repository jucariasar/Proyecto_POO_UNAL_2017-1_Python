

class Empleado:
    tiposEmpleado = {'1':'Administrador Almacen','2':'Administrativo', 
    '3':'Ingeniero Tecnico', 
    '4':'Operario'} # Diccionario estatico para estandarizar los tipos
    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll=0, email=""):
        self._ident = ident
        self._nombre = nombre
        self._apellido = apellido
        self._numElementPrest = numElementPrest
<<<<<<< HEAD
        self._numRestriccion = 0 # Variable nueva, para que entre reservas y prestamos un usuario no pueda prestar masde lo que su rol le permite
=======
>>>>>>> refs/remotes/origin/Version_1
        self._roll = roll  # Son los tipos del diccionario tiposEmpleado
        self._contador = 0
        self._email = email
        self._elementos = []

    def getIdent(self):
        return self._ident

    def setIdent(self, ident):
        self._ident = ident

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getApellido(self):
        return self._apellido

    def setApellido(self, apellido):
        self._apellido = apellido

    def getNumElementPres(self):
        return self._numElementPrest

    def setNumElementPres(self, num):
        self._numElementPrest = num

    def getRoll(self):
        return self._roll

    def setRoll(self, roll):
        self._roll = roll

    def getContador(self):
        return self._contador

    def setContador(self, contador):
        self._contador = contador

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

<<<<<<< HEAD
    def getElementos(self):
        return self._elementos

    def getNumRestriccion(self):  # Retorna valor de Variable Nueva
        return self._numRestriccion

    def setNumRestriccion(self, num): # Establece Valor de Variable Nueva
        self._numRestriccion = num

    def setAddElemento(self, elem):
        self._elementos.append(elem)

    def setDelElemento(self, elem):
        self._elementos.remove(elem)

    def __str__(self):
        return("Nombre del Empleado: " + self.getNombre() + " " + self.getApellido() + 
            "\nN° Identificacion: " + str(self.getIdent()) + "\nRoll: " + self.getRoll() +
            "\nN° de Elementos Prestados: " + str(self.getNumElementPres())+'\n'+"E-mail: "+self.getEmail())
=======
    def __str__(self):
        return("\n Nombre del Empleado: " + str(self.getNombre()) + " " + str(self.getApellido()) + 
            "\n N° Identificacion: " + str(self.getIdent()) + "\nRoll: " + str(self.getRoll()) +
            "\n N° de Elementos Prestados: " + str(self.getNumElementPres())+"\n E-mail: "+str(self.getEmail()))
>>>>>>> refs/remotes/origin/Version_1

    def str_Empleado(self):
        return(" Nombre del Empleado: " + str(self.getNombre()) + " " + str(self.getApellido()) + 
            "\n N° Identificacion: " + str(self.getIdent()) + "\n Roll: " + str(self.getRoll()) +
            "\n E-mail: "+str(self.getEmail()))
<<<<<<< HEAD

# Inicio de métodos estaticos agregados por Camilo
    @staticmethod
    def imprimirEmpleados(lis):
        for e in lis:
            print(e)

    @staticmethod
    def buscarEmpleadoPorId(listado, i):
        for e in listado:
            if (e.getIdent() == i):
                return e
        return None
# Fin de métodos estaticos agregados por  Camilo

# Inicio de Métodos estáticos agregados por Pablo y Jaider

    @staticmethod
    def masElemPrestados(listado):
=======
    @staticmethod
    def MasPrestado(listado):
>>>>>>> refs/remotes/origin/Version_1
        elempres=0
        emp=""
        for e in listado:
            if (e.getNumElementPres()>elempres):
                elempres=e.getNumElementPres()
                emp=e
        if(emp!=""):
            print("El empleado con mas elementos prestados es: ")
            print ("\n"+str(emp.getNombre())+" "+str(emp.getApellido()) + " >> "+"N° elementos prestado: "+str(emp.getNumElementPres()))
        else:
            print("Ningun empleado ha prestado elementos")

<<<<<<< HEAD

    @staticmethod
    def masValorPrestado(listado):
        mayor=0
        emp=""
        for e in listado:
            suma=0
            for j in e.getElementos():
                if j.getEstadoActual()=="Prestado" : # Problemas con la importacion
                    suma=j.getValor()+suma
            if suma>mayor:
                mayor=suma
                emp=e
        if emp!="":
            print("\n El empleado con mas Valor Prestado es: "+emp.getNombre()+" "+emp.getApellido())
            print("\n El valor total prestado por el empleado actualmente es: "+ str(mayor) )
        elif emp=="":
            print("\n Aun no han sido prestado elementos con valor ")


    @staticmethod
    def listadoEmpleados(listado):
        print("La base de datos actual de empleados es: ")
        for emp in listado:
            print(emp.str_Empleado()) ## 


    @staticmethod
    def masHaPrestado(listado):
        elemPrest=0
        emp=""
        for e in listado:
            if (e.getContador()>elemPrest):
                elemPrest=e.getContador()
                emp=e
        if(emp!=""):
            print("El empleado que mas ha prestado elementos es: ")
            print ("\n"+str(emp.getNombre())+" "+emp.getApellido()+" >> "+"N° veces que ha prestado: "+str(emp.getContador()))
        else:
            print("\n Ningun elemento ha sido prestado")



    @staticmethod
    def rollEstrella(listado):
        elemPrest1=0
        elemPrest2=0
        elemPrest3=0
        elemPrest4=0
        for e in listado:
            if (e.getRoll()==Empleado().tiposEmpleado['1']):
                elemPrest1=e.getContador()+elemPrest1
                
            elif (e.getRoll()==Empleado().tiposEmpleado['2']):
                elemPrest2=e.getContador()+elemPrest2

            elif(e.getRoll()==Empleado().tiposEmpleado['3']):
                elemPrest3=e.getContador()+elemPrest3

            elif (e.getRoll()==Empleado().tiposEmpleado['4']):
                elemPrest4=e.getContador()+elemPrest4

        roll=max(elemPrest1,elemPrest2,elemPrest3,elemPrest4)   
        if(roll>0):
            if(roll==elemPrest1):
                print("El roll que mas ha prestado elementos es: ")
                print ("\n"+Empleado().tiposEmpleado['1']+" >> "+"N° veces que han prestado: "+str(elemPrest1))
            elif(roll==elemPrest2):
                print("El roll que mas ha prestado elementos es: ")
                print ("\n"+Empleado().tiposEmpleado['2']+" >> "+"N° veces que han prestado: "+str(elemPrest2))
            elif(roll==elemPrest3):
                print("El roll que mas ha prestado elementos es: ")
                print ("\n"+Empleado().tiposEmpleado['3']+" >> "+"N° veces que han prestado: "+str(elemPrest3))
            elif(roll==elemPrest4):
                print("El roll que mas ha prestado elementos es: ")
                print ("\n"+Empleado().tiposEmpleado['4']+" >> "+"N° veces que han prestado: "+str(elemPrest4))
        else:
            print("\n Ningun elemento ha sido prestado")

# Fin de métodos estáticos agregados por Pablo y Jaider
=======
    @staticmethod
    def ListadoEmpleados(listado):
            print("La base de datos actual de empleados es: ")
            for emp in listado:
                    print(emp.str_Empleado())

    @staticmethod
    def buscarEmpleadoPorId(listado, i):
        for e in listado:
            if (e.getIdent() == i):
                return e
        return None


>>>>>>> refs/remotes/origin/Version_1
