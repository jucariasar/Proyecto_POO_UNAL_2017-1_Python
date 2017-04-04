from empleado import Empleado

class Operario(Empleado):
<<<<<<< HEAD
    MAX_OP = 6 # Constante de clase para controlar el numero máximo de elementos que puede
=======
    MAX_OP = 15 # Constante de clase para controlar el numero máximo de elementos que puede
>>>>>>> refs/remotes/origin/Version_1
                # prestar un operario
    tipo = {'1':'Mecanico', 
    '2':'Electrico', '3':'Electronico'} # Diccionario estatico para estandarizar los tipos de Operarios

    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll="", email="", tipo=""):
        super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
        self._tipo = tipo # Los tipos definidos en el diccionario estatico de tipo

    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo

<<<<<<< HEAD
    
    @staticmethod
    def registrarEmpleado(listEmpleados):
        empleado = Operario()
        empleado.setIdent(int(input("Ingrese el id del operario:")))
        empleado.setNombre(str(input("Ingrese el nombre del operario:"))) 
        empleado.setApellido(str(input("Ingrese el apellido del operario:")))
        empleado.setEmail(str(input("Ingrese el correo del operario:")))
        empleado.setRoll(Empleado().tiposEmpleado['4'])
        empleado.setTipo(str(input("Establezca el tipo de operario:")))
        listEmpleados.append(empleado)






=======
>>>>>>> refs/remotes/origin/Version_1
    def __str__(self):
        return(super().__str__() + "\nTipo: " + self.getTipo())