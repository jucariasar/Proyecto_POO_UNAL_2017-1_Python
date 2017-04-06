from empleado import Empleado
from mensajes import Mensaje

class Operario(Empleado):
    MAX_OP = 6
                
    tipo = {'1':'Mecanico', 
    '2':'Electrico', '3':'Electronico'}

    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll="", email="", tipo=""):
        super().__init__(ident, nombre, apellido, numElementPrest, roll, email)
        self._tipo = tipo # Los tipos definidos en el diccionario estatico de tipo

    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo

    
    @staticmethod
    def registrarEmpleado(listEmpleados):
        empleado = Operario()
        empleado.setIdent(int(input(Mensaje.obtenerMensaje('setIdOp'))))
        
        while Empleado().buscarEmpleadoPorId(listEmpleados, empleado.getIdent()) != None:
            Mensaje.mostrarMensajes('yaExistEmp')
            empleado.setIdent(int(input(Mensaje.obtenerMensaje('setIdOp'))))

        empleado.setNombre(str(input(Mensaje.obtenerMensaje('setNomOp')))) 
        empleado.setApellido(str(input(Mensaje.obtenerMensaje('setApellOp'))))
        empleado.setEmail(str(input(Mensaje.obtenerMensaje('setEmailOp'))))
        empleado.setRoll(Empleado().tiposEmpleado['4'])
        empleado.setTipo(str(input(Mensaje.obtenerMensaje('setTipo'))))
        listEmpleados.append(empleado)


    def __str__(self):
        return(super().__str__() + "\nTipo: " + self.getTipo())