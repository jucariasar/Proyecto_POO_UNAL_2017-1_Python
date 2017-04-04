from administrativo import Administrativo

class AdministradorAlmacen(Administrativo):
    def __init__(self, ident=0, nombre="", apellido="", numElementPrest=0, roll="", email="", grado=0, 
    usuario="", password=""):
        super().__init__(ident, nombre, apellido, numElementPrest, roll, email, grado)
        self._usuario = usuario
        self._password = password
    def getUsuario(self):
        return self._usuario
    def setUsuario(self,usuario):
        self._usuario=usuario
        
    def getPassword(self):
        return self._password
    def setPassword(self,password):
        self._password=password
        
    
    @staticmethod
    def registrarEmpleado(listEmpleados):
        
        print("\n¿Empleado Administrador del almacen?")
        print("1. Si.")
        print("2. No.")
        op = input("\nIngrese su opcion: ")
        if op == '1':
               empleado = AdministradorAlmacen()
               empleado.setUsuario(str(input("Establezca el usuario:")))
               empleado.setPassword(str(input("Establezca el password:")))
               empleado.setRoll('Administrador Almacen')
        else:
               empleado = Administrativo()
               empleado.setRoll('Administrativo')
               
        
        empleado.setIdent(int(input("Ingrese el id del Administrador:")))
        empleado.setNombre(str(input("Ingrese el nombre del Administrador:"))) 
        empleado.setApellido(str(input("Ingrese el apellido del Admnistrador:")))
        empleado.setEmail(str(input("Ingrese el correo del Administrador:")))
        empleado.setGrado(str(input("Establezca el grado del Administrador: ")))
        listEmpleados.append(empleado)






    def __str__(self):
        retrun (super().__str__()+'\n'+"Usuario: "+self.getUsuario()+'\n'+"Password: "+self.getPassword())