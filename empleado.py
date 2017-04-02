

class Empleado:
    tiposEmpleado = {'1':'Administrador Almacen','2':'Administrativo', 
    '3':'Ingeniero Tecnico', 
    '4':'Operario'} # Diccionario estatico para estandarizar los tipos
    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll=0, email=""):
        self._ident = ident
        self._nombre = nombre
        self._apellido = apellido
        self._numElementPrest = numElementPrest
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

    def __str__(self):
        return("Nombre del Empleado: " + self.getNombre() + " " + self.getApellido() + 
            "\nN° Identificacion: " + str(self.getIdent()) + "\nRoll: " + self.getRoll() +
            "\nN° de Elementos Prestados: " + str(self.getNumElementPres())+'\n'+"E-mail: "+self.getEmail())

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

    