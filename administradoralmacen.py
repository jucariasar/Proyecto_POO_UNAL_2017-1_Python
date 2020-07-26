from funcionesvalidacion import comprobarCorreoValido
from administrativo import Administrativo, Empleado, Mensaje, system, path
from random import randint
#from importacion1 import Administrativo, Empleado, Mensaje, system, path, comprobarCorreoValido, comprobarExistenciaCorreo, generarUsuario
#comprobarCorreoValido, comprobarExistenciaCorreo, generarUsuario
#from elemento import Elemento
#from empleado import Empleado, system, path
#from mensajes import Mensaje

class AdministradorAlmacen(Administrativo):
    def __init__(self, ident = 0, nombre = "", apellido = "", numElementPrest = 0, roll = "", email = "", grado = 0, 
    usuario = "", password = ""):
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
    

    def __str__(self):
        return (super().__str__()+'\n'+"Usuario: "+self.getUsuario()+'\n'+"Password: "+self.getPassword())
    

    @staticmethod
    def registrarAdministrador(listEmpleados):
        salir = False
        quePaso = 0
        while salir == False:
            #system("cls")
            Mensaje.mostrarMensajes('registAdminAlmacen')
            op = input(Mensaje.obtenerMensaje('optIn'))
            #empleado = None
            system("cls")
            if op == '1':
                empleado = AdministradorAlmacen()
                correo = False
                while correo == False:
                    email = input(Mensaje.obtenerMensaje('emailIn'))
                    if comprobarCorreoValido(email):
                        if AdministradorAlmacen().comprobarExistenciaCorreo(listEmpleados, email):
                            Mensaje.mostrarMensajes('replayEmail')
                            continue
                        else:
                            user = AdministradorAlmacen().generarUsuario(listEmpleados, email)
                            empleado.setEmail(email.lower())
                            empleado.setUsuario(user)
                            Mensaje.mostrarEmail('emailAsign', empleado.getEmail())
                            Mensaje.mostrarUsuarioAsignado('userAsign', empleado.getUsuario())
                            correo = True
                    else:
                        system("cls")
                        Mensaje.mostrarMensajes('correoInvalido')
                        Mensaje.mostrarMensajes('intentarNuevo')

                
                empleado.setPassword(str(input(Mensaje.obtenerMensaje('setPassd'))))
                empleado.setRoll(Empleado().tiposEmpleado['1'])
            elif op == '2':
                empleado = Administrativo()
                empleado.setRoll('Administrativo')
            elif op == '3':
                return None
            else:
                Mensaje.mostrarMensajes('optInvalid')
                continue
            
            validIdent = False
            while validIdent == False:
                try:
                    empleado.setIdent(int(input(Mensaje.obtenerMensaje('setIdAdmin'))))
                except ValueError:
                    #system("cls")
                    Mensaje.mostrarMensajes('optInvalid')
                    continue
                
                if Empleado().buscarEmpleadoPorId(listEmpleados, empleado.getIdent()) != None:
                    Mensaje.mostrarMensajes('yaExistEmp')
                    #empleado.setIdent(int(input(Mensaje.obtenerMensaje('setIdAdmin'))))
                else:
                    validIdent = True
                # Implementar una forma de salir si se quiere.
        
            if(isinstance(empleado, AdministradorAlmacen)):
                pass
            else:
                while correo == False:
                    email = input(Mensaje.obtenerMensaje('emailIn'))
                    if comprobarCorreoValido(email):
                        if comprobarExistenciaCorreo(listEmpleados, email):
                            Mensaje.mostrarMensajes('replayEmail')
                            continue
                        else:
                            empleado.setEmail(email)
                            Mensaje.mostrarEmail('emailAsign', empleado.getEmail())
                            correo = True
                    else:
                        system("cls")
                        Mensaje.mostrarMensajes('correoInvalido')
                        Mensaje.mostrarMensajes('intentarNuevo')


            empleado.setNombre(str(input(Mensaje.obtenerMensaje('setNomAdmin'))).lower()) 
            empleado.setApellido(str(input(Mensaje.obtenerMensaje('setApellAdmin'))).lower())
            # Verificar email valido
            #empleado.setEmail(str(input(Mensaje.obtenerMensaje('setEmailAdmin'))))
            # Verificar grado. (Crear lista de gados)
            empleado.setGrado(str(input(Mensaje.obtenerMensaje('setGradAdmin'))))
            listEmpleados.append(empleado)
            return 1


    @staticmethod
    def menuAdministradorAlmacen(empleados, elementos):
        salir = False
        system("color 0A")
        while(salir == False):
            system("cls")
            Mensaje.mostrarMensajes('menuPpalAdmin')
            op = input(Mensaje.obtenerMensaje('optIn')) # Acá voy revisando
            if op == "1":
                AdministradorAlmacen().subMenu1AdministradorAlmacen(empleados, elementos)
            elif op == "2":
                AdministradorAlmacen().subMenu2AdministradorAlmacen(empleados, elementos)
            elif op == "3":
                AdministradorAlmacen().menu3AdministradorAlmacen()
            elif op == "4":
                system("cls")
                salir = True
            else:
                system("cls")
                Mensaje.mostrarMensajes('optInvalid')


    # Menú de consultas
    @staticmethod
    def subMenu1AdministradorAlmacen(empleados, elementos):
        salir = False
        system("cls")
        system("color 0A")
        while(salir == False):
        
            Mensaje.mostrarMensajes('menu1Admin')
        
            try:
                op = int(input(Mensaje.obtenerMensaje('optIn')))
                system("cls")
                system("color 0A")
                if(op == 1):

                    Elemento().inventarioElementos(elementos)
                elif(op == 2):
            
                    Empleado().listadoEmpleados(empleados)
                elif(op == 3):
            
                    Elemento().masPrestado(elementos)
                elif(op == 4):
            
                    Elemento().cincoMasPrestados(elementos)
                elif(op == 5):
            
                    Empleado().masElemPrestados(empleados)
                elif(op == 6):
            
                    Empleado().masValorPrestado(empleados)
                elif(op == 7):
            
                    Empleado().masHaPrestado(empleados)
                elif(op == 8):
            
                    Empleado().rollEstrella(empleados)
                elif(op == 9):
            
                    salir = True
                else:
                    system("cls")
                    system("color 0A")
                    Mensaje.mostrarMensajes('optInvalid')
            except ValueError:
                system("cls")
                system("color 0A")
                Mensaje.mostrarMensajes('optInvalid')

    # Revisando
    
    @staticmethod
    def subMenu2AdministradorAlmacen(empleados, elementos):
        salir = False
        system("color 0A")
        system("cls")
        while salir == False :

            Mensaje.mostrarMensajes('menu2Admin')
            op = input(Mensaje.obtenerMensaje('optIn'))
            if op == "1":
                system("cls")
                AdministradorAlmacen().menuRegistrarEmpleado(empleados)
            elif op == "2":
                system("cls")
                Elemento().registrarElemento(self)
        
            elif op == "3":
                system("cls")
                salir = False
                while salir == False:    
                   
                    i = int(input(Mensaje.obtenerMensaje('idIn')))
                        
                    emp = Empleado().buscarEmpleadoPorId(empleados, i) 
                   
                    if emp != None:
                        if (Elemento().verificarPrestamo(emp.getElementos())):
                            Mensaje.mostrarMensajes('empNoPuedeSerEliminado1')
                            
                        elif(Elemento().verificarReserva(emp.getElementos())):
                            Mensaje.mostrarMensajes('eliminacionEmp1')
                            Elemento().cancelarReserva(emp.getElementos())
                            Mensaje.mostrarMensajes('eliminacionEmpOk')
                            self._empleados.remove(emp)
                        else:
                            Mensaje.mostrarMensajes('eliminacionEmpOk')
                            self._empleados.remove(emp)
                    else:
                        Mensaje.mostrarMensajes('empNoRegistrado')
                    respuesta = input(Mensaje.obtenerMensaje('seguirEliminandoEmp')) 
                    if(respuesta == 'n') :
                      salir = True    
           

            elif op == "4":        
                    system("cls")
                    system("color 0A")
                    salir = False
                    while salir == False:   
                        i = int(input("Ingrese el codigo  del elemento: "))
                        elm = Elemento().buscarElementoPorId(elementos, i)
                        
                        if elm != None:
                            if (Elemento().verificarPrestamo(elementos)):
                                Mensaje.mostrarMensajes('elementNoPuedeSerEliminado1')
                            elif(Elemento().verificarReserva(elementos)):
                                Mensaje.mostrarMensajes('eliminacionElement1')
                                Elemento().cancelarReserva(elementos)
                                Mensaje.mostrarMensajes('eliminacionElementOk')
                                self._elementos.remove(elm)
                            else:
                                Mensaje.mostrarMensajes('eliminacionElementOk')
                                self._elementos.remove(elm)
                        else:
                            Mensaje.mostrarMensajes('elementNoRegistr')
                        respuesta = input(Mensaje.obtenerMensaje('seguirEliminandoElement')) 
                        if(respuesta == 'n') :
                          salir = True 

            elif op == "5":
                salir = True
            else:
                Mensaje.mostrarMensajes('optInvalid')


    @staticmethod
    def menuRegistrarEmpleado(empleados):
        salir = False
        quePaso = 0 #LineaNueva
        while salir == False:

            Mensaje.mostrarMensajes('registEmp1')
            op = input(Mensaje.obtenerMensaje('optIn'))
            if op == '1':
               quePaso = AdministradorAlmacen().registrarAdministrador(empleados)
            elif op == '2' :
                Operario().registrarEmpleado(empleados)
            elif op == '3' :
                IngenieroTecnico().registrarEmpleado(empleados)
            elif op == '4' :
                salir = True
                system("cls")
                break
            else:
                Mensaje.mostrarMensajes('optInvalid')

            if quePaso != None:
                Mensaje.mostrarMensajes('registroEmpOk')
                respuesta = input(Mensaje.obtenerMensaje('seguirRegistEmp')) 
                if(respuesta == 'n') :
                    system("cls")
                    salir = True


    @staticmethod
    def comprobarExistenciaCorreo(empleados, email):
        for emp in empleados:
            if emp.getEmail() == email:
                return True
        return False

    @staticmethod
    def generarUsuario(empleados, email):
        correo1 = email.lower()
        separacion = correo1.split('@')
        usuario = separacion[0]
    
        while AdministradorAlmacen().verificarUsuario(empleados, usuario):
            usuario = AdministradorAlmacen().generarNuevoUsuario(usuario)
        return usuario

    @staticmethod
    def verificarUsuario(empleados, usuario):
        for emp in empleados:
            if isinstance(emp, AdministradorAlmacen):
                if emp.getUsuario() == usuario:
                    return True
        return False

    @staticmethod
    def generarNuevoUsuario(usuario):
        complemento = str(randint(1, 800))
        user = usuario + complemento
        return user