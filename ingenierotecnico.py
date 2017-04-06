from empleado import Empleado

class IngenieroTecnico(Empleado):
    MAX_IT = 4 # Constante de clase para controlar el numero máximo de elementos que puede prestar 
                #un IngenieroTecnico
    areas = {'1':'Mantenimiento', '2':'Produccion', 
    '3':'Calidad'}
    
    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll="", email="", area=""):
        super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
        self._areaEncargada = area # Los tipos definidos en el diccionario estatico de areas

    def getArea(self):
        return self._areaEncargada

    def setArea(self, area):
        self._areaEncargada = area

    @staticmethod
    def registrarEmpleado(listEmpleados):
        empleado = IngenieroTecnico()
        empleado.setIdent(int(input("Ingrese el id del ingeniero:")))
        while Empleado().buscarEmpleadoPorId(listEmpleados, empleado.getIdent()) != None:
            print(" \n!!! Ya existe un empleado con este numero de identificacion !!!")
            empleado.setIdent(int(input("Ingrese el id del ingeniero:")))
        empleado.setNombre(str(input("Ingrese el nombre del ingeniero:"))) 
        empleado.setApellido(str(input("Ingrese el apellido del ingeniero:")))
        empleado.setEmail(str(input("Ingrese el correo del ingeniero:")))
        empleado.setRoll(Empleado().tiposEmpleado['3'])
        empleado.setArea(str(input("Establezca area del Ingeniero:")))
        listEmpleados.append(empleado)






    def __str__(self):
        return (super().__str__() + "\nArea Encargada: " + self.getArea())
