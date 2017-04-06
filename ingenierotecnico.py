from empleado import Empleado
from mensajes import Mensaje

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
        empleado.setIdent(int(input(Mensaje.obtenerMensaje('setIdIng'))))
        while Empleado().buscarEmpleadoPorId(listEmpleados, empleado.getIdent()) != None:
            Mensaje.mostrarMensajes('yaExistEmp')
            empleado.setIdent(int(input(Mensaje.obtenerMensaje('setIdIng'))))
        empleado.setNombre(str(input(Mensaje.obtenerMensaje('setNomIng')))) 
        empleado.setApellido(str(input(Mensaje.obtenerMensaje('setApellIng'))))
        empleado.setEmail(str(input(Mensaje.obtenerMensaje('setEmailIng'))))
        empleado.setRoll(Empleado().tiposEmpleado['3'])
        empleado.setArea(str(input(Mensaje.obtenerMensaje('setAreaIng'))))
        listEmpleados.append(empleado)

    def __str__(self):
        return (super().__str__() + "\nArea Encargada: " + self.getArea())
