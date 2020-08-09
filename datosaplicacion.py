from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from elemento import Elemento
from os import path

def guardarDatosEmpleados(empleados):

    archivo_empleados = path.join("Datos", "empleados.csv") #Para Linux o Windows
    if path.isfile(archivo_adoemples): #Si el archivo existe
        archivo = open(archivo_empleados, 'a')
    else: # Si el archivo no exite
        archivo = open(archivo_empleados, 'w')
        lineas = ["Documento,","Nombres,","Apellidos,","Elementos_prestados,","Roll,","Email,","Grado,","Usuario,","Password,","Area,","Tipo\n"]
        archivo.writelines(lineas)

    
    for e in empleados:
        archivo.write(str(e.getIdent())+",")
        archivo.write(e.getNombre()+",")
        archivo.write(e.getApellido()+",")
        archivo.write(str(e.getNumElementPres())+",")
        archivo.write(e.getRoll()+",")
        archivo.write(e.getEmail()+",")
        if isinstance(e, AdministradorAlmacen):
            archivo.write(str(e.getGrado())+",")
            archivo.write(e.getUsuario()+",")
            archivo.write(e.getPassword()+",")
            archivo.write("Null,")
            archivo.write("Null\n",)
        elif isinstance(e, Administrativo):
            archivo.write(str(e.getGrado())+",")
            archivo.write("Null,")
            archivo.write("Null,")
            archivo.write("Null,")
            archivo.write("Null\n",)
        elif isinstance(e, IngenieroTecnico):
            archivo.write("Null,")
            archivo.write("Null,")
            archivo.write("Null,")
            archivo.write(e.getArea()+",")
            archivo.write("Null\n",)
        else:
            archivo.write("Null,")
            archivo.write("Null,")
            archivo.write("Null,")
            archivo.write("Null,")
            archivo.write(e.getTipo()+"\n")

    archivo.close()

"""
def guardarEmpleadoEnArchivo(empleado):
    archivo_empleados = path.join("Datos", "empleados.csv") #Para Linux o Windows
    archivo = open(archivo_empleados, 'a')
    archivo.write(str(empleado.getIdent())+",")
    archivo.write(empleado.getNombre()+",")
    archivo.write(empleado.getApellido()+",")
    archivo.write(str(empleado.getNumElementPres())+",")
    archivo.write(empleado.getRoll()+",")
    archivo.write(empleado.getEmail()+",")
    if isinstance(empleado, AdministradorAlmacen):
        archivo.write(str(empleado.getGrado())+",")
        archivo.write(empleado.getUsuario()+",")
        archivo.write(empleado.getPassword()+",")
        archivo.write("Null,")
        archivo.write("Null\n",)
    elif isinstance(empleado, Administrativo):
        archivo.write(str(empleado.getGrado())+",")
        archivo.write("Null,")
        archivo.write("Null,")
        archivo.write("Null,")
        archivo.write("Null\n",)
    elif isinstance(empleado, IngenieroTecnico):
        archivo.write("Null,")
        archivo.write("Null,")
        archivo.write("Null,")
        archivo.write(empleado.getArea()+",")
        archivo.write("Null\n",)
    else:
        archivo.write("Null,")
        archivo.write("Null,")
        archivo.write("Null,")
        archivo.write("Null,")
        archivo.write(empleado.getTipo()+"\n")

    archivo.close()
"""

def guardarDatosElementos(elementos):
    archivo_elementos = path.join("Datos", "elementos.csv") #Para Linux o Windows
    if path.isfile(archivo_elementos): #Si el archivo existe
        archivo = open(archivo_elementos, 'a')
    else: # Si el archivo no exite
        archivo = open(archivo_elementos, 'w')
        lineas = ["Codigo,","Descripcion,","Modelo,","Marca,","Ubicacion,","Fecha_de_Prestamo,","Valor,","Estado_Actual\n"]
        archivo.writelines(lineas)

    for elem in elementos:
        archivo.write(str(elem.getCodigo())+",")
        archivo.write(elem.getDescripcion()+",")
        archivo.write(elem.getModelo()+",")
        archivo.write(str(elem.getMarca())+",")
        archivo.write(elem.getUbicacion()+",")
        archivo.write(str(elem.getFechaPrestamo())+",")
        archivo.write(str(elem.getValor())+",")
        archivo.write(elem.getEstadoActual()+"\n")

    archivo.close()

def cargarDatosEmpleados(empleados):
    esquema = {'Documento':0,'Nombres':1,'Apellidos':2,'Elementos_prestados':3,'Roll':4,'Email':5,
    'Grado':6,'Usuario':7,'Password':8,'Area':9,'Tipo':10}
    archivo_empleados = path.join("Datos", "empleados.csv") # Para Linux o Windows
    if path.isfile(archivo_empleados): # Si el archivo existe
        archivo = open(archivo_empleados, 'r') # Abre el archivo para lectura
        archivo.seek(0) # Posiciona el apuntador al inicio del archivo.
        roll = 0
        cont = 0
        for dato in archivo:
            if(cont == 0):
                encabezado = dato.split(",")
                roll = posicionRoll(encabezado)
                cont+=1
                continue
            empleado = dato.split(",")

            if empleado[roll] == "Administrador Almacen":
                e = crearAdministradorAlmacen(empleado, esquema) # Crear funcion
            elif empleado[roll] == "Administrativo":
                e = crearAdministrativo(empleado, esquema) # Crear funcion
            elif empleado[roll] == "Ingeniero Tecnico":
                e = crearIngenieroTecnico(empleado, esquema) # Crear funcion
            elif empleado[roll] == "Operario":
                e = crearOperario(empleado, esquema) # Crear funcion

            empleados.append(e)

        archivo.close()
        #print("Empleados Cargados con Éxito !!!")
    else: # Si el archivo no exite
        print("No Existe Archivo para Cargar los Empleados.")


def cargarDatosElementos(elementos):
    esquema = {'Codigo':0,'Descripcion':1,'Modelo':2,'Marca':3,'Ubicacion':4,'Fecha_de_Prestamo':5,
    'Valor':6,'Estado_Actual':7}
    archivo_elementos = path.join("Datos", "elementos.csv") # Para Linux o Windows
    if path.isfile(archivo_elementos): # Si el archivo existe
        archivo = open(archivo_elementos, 'r') # Abre el archivo para lectura
        archivo.seek(0) # Posiciona el apuntador al inicio del archivo.
        cont = 0
        for dato in archivo:
            if(cont == 0):
                encabezado = dato.split(",")
                cont+=1
                continue
            element = dato.replace("\n","")
            elemento = element.split(",")
            #print(elemento)
            elem = crearElemento(elemento, esquema)
            elementos.append(elem)

        archivo.close()
        #print("Elementos Cargados con Éxito !!!")
    else: # Si el archivo no exite
        print("No Existe Archivo para Cargar los Elementos.")

def posicionRoll(encabezado):
    cont = 0
    for i in encabezado:
        if i == "Roll":
            return cont
        cont+=1

def crearAdministradorAlmacen(empleado, esquema):
    e = AdministradorAlmacen()
    e.setIdent(int(empleado[esquema['Documento']]))
    e.setNombre(empleado[esquema['Nombres']])
    e.setApellido(empleado[esquema['Apellidos']])
    e.setNumElementPres(int(empleado[esquema['Elementos_prestados']]))
    e.setRoll(empleado[esquema['Roll']])
    e.setEmail(empleado[esquema['Email']])
    e.setGrado(int(empleado[esquema['Grado']]))
    e.setUsuario(empleado[esquema['Usuario']])
    e.setPassword(empleado[esquema['Password']])
    return e

def crearAdministrativo(empleado, esquema):
    e = Administrativo()
    e.setIdent(int(empleado[esquema['Documento']]))
    e.setNombre(empleado[esquema['Nombres']])
    e.setApellido(empleado[esquema['Apellidos']])
    e.setNumElementPres(int(empleado[esquema['Elementos_prestados']]))
    e.setRoll(empleado[esquema['Roll']])
    e.setEmail(empleado[esquema['Email']])
    e.setGrado(int(empleado[esquema['Grado']]))
    return e

def crearIngenieroTecnico(empleado, esquema):
    e = IngenieroTecnico()
    e.setIdent(int(empleado[esquema['Documento']]))
    e.setNombre(empleado[esquema['Nombres']])
    e.setApellido(empleado[esquema['Apellidos']])
    e.setNumElementPres(int(empleado[esquema['Elementos_prestados']]))
    e.setRoll(empleado[esquema['Roll']])
    e.setEmail(empleado[esquema['Email']])
    e.setArea(empleado[esquema['Area']])
    return e

def crearOperario(empleado, esquema):
    e = Operario()
    e.setIdent(int(empleado[esquema['Documento']]))
    e.setNombre(empleado[esquema['Nombres']])
    e.setApellido(empleado[esquema['Apellidos']])
    e.setNumElementPres(int(empleado[esquema['Elementos_prestados']]))
    e.setRoll(empleado[esquema['Roll']])
    e.setEmail(empleado[esquema['Email']])
    e.setTipo(empleado[esquema['Tipo']])
    return e

def crearElemento(elemento, esquema):
    elem = Elemento()
    elem.setCodigo(int(elemento[esquema['Codigo']]))
    elem.setDescripcion(elemento[esquema['Descripcion']])
    elem.setModelo(elemento[esquema['Modelo']])
    elem.setMarca(elemento[esquema['Marca']])
    elem.setUbicacion(elemento[esquema['Ubicacion']])
    elem.setFechaPrestamo(elemento[esquema['Fecha_de_Prestamo']])
    elem.setValor(elemento[esquema['Valor']])
    elem.setEstadoActual(str(elemento[esquema['Estado_Actual']]))
    return elem

def comprobarArchivo(ruta, nombre):
    archivo_empleados = path.join(ruta, nombre)

    if path.isfile(archivo_empleados):
        return True
    else:
        return False