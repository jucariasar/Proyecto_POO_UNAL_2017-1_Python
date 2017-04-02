from empleado import Empleado

class IngenieroTecnico(Empleado):
    MAX_IT = 10 # Constante de clase para controlar el numero máximo de elementos que puede prestar 
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

    def __str__(self):
        return (super().__str__() + "\nArea Encargada: " + self.getArea())
