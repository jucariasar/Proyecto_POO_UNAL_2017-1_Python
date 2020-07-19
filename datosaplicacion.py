from empleado import Empleado
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario
from administradoralmacen import AdministradorAlmacen
from os import path

def guardarDatos(empleados):

	archivo_empleados = path.join("Datos", "empleados.csv") #Para Linux o Windows
	#archivo_elementos = path.join("Datos", "elementos.csv")
	if path.isfile(archivo_empleados): #Si el archivo existe
		archivo = open(archivo_empleados, 'a')
	else: # Si el archivo no exite
		archivo = open(archivo_empleados, 'w')
		lineas = ["documento,","Nombres,","Apellidos,","Elementos_prestados,","Roll,","Email,","Grado,","Usuario,","Password,","Area,","Tipo\n"]
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
	print("Datos Guardados con Éxito !!!")
		