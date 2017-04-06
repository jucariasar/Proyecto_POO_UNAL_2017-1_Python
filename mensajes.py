#from administradoralmacen import AdministradorAlmacen
#from empleado import Empleado
##from administrativo import Administrativo
##from ingenierotecnico import IngenieroTecnico
#from operario import Operario

class Mensaje():
	mensaje = {
	'bienvenida':'\nBienvenido ',
	'optInvalid':'\n ¡¡¡ Opcion Invalida !!!',
	'menuPpal':'\n\n1. Crear Datos Ficticios.\n2. Crear Datos Ficiticos Desde un txt.\n3. Escribir Datos Ficiticos En un txt.\n4. Ingresar al Sistema.\n5. Salir',
	'menuPpalAdmin':'\nMenu de Usuario Administrador del Almacen:\n\n1. Ir al Menu de Consultas.\n2. Ir al Menu de Registros / Borrados.\n3. Prestar / Recibir.\n4. Cerrar Sesion de Administrador.',
	'menu1Admin':'\n\n¿Que Consulta Desea Realizar?\n\n1. Consultar Inventario de Elementos.\n2. Consultar Base de Datos de Empleados.\n3. Consultar el Elemento mas Prestado.\n4. Consultar los 5 Elementos mas Prestados.\n5. Consultar Empleado con mas Elementos Prestados.\n6. Consultar Empleados con mas Valor Prestado.\n7. Consultar el Empleado que mas Presta.\n9. Volver al Menu Anterior.',
	'menu2Admin':'\n\n¿Que desea hacer?\n\n1. Registrar Empleado.\n2. Registrar Elemento.\n3. Eliminar Empleado.\n4. Eliminar Elemento.\n5. Volver al Menu Anterior.',
	'menu3Admin':'\n\n¿Que desea hacer?:\n\n1. Prestar Elementos.\n2. Recibir Elementos.\n3. Mostrar Historial.\n4. Volver al Menu Anterior.',
	'menuEmpleado':'\n¿Que desea hacer?\n\n1. Consultar Elementos Disponibles.\n2. Consultar Elementos Prestados.\n3. Reservar Elementos para Prestar.\n4. Modificar Reserva de Elementos.\n5. Cerrar Sesion de Usuario.',
	'SelectRollAdmin':'\n\nCon que Roll Desea Ingresar:\n\n1. Como Administrador del Almacen.\n2. Como Empleado NO Administrador.\n3. Desea volver al menu principal.',
	'infoAdmin1':'\nA continuacion debe de ingresar su usuario y contraseña para ingresar a administrar la aplicacion\n',
	'registEmp1':'\n¿Qué tipo de empleado desea registrar?\n\n1.Empleado Administrativo.\n2.Empleado Operario.\n3.Ingeniero Tecnico.\n4.Regresar al Menu anterior',
	'menu3Opt1':'\n El usuario actualmente tiene elemento(s) reservado(s): \n\n ¿Que Desea Hacer?:\n\n 1. Asentar la reserva.\n 2. Prestar nuevos elementos.\n 3. Volver.',
	'emailDocumentInvalid':'\n\nE-mail y/o Documento Invalido\n\n',
	'userPassInvalid':'\n Usuario y/o Passwor Incorrecto.\n',
	'empNoPuedeSerEliminado1':'\n El empleado tiene elementos prestados. No puede ser eliminado\n',
	'eliminacionEmp1':'\nEl empleado tiene elementos reservados.Estos pasaran a estar disponibles\n',
	'eliminacionEmpOk':'\n !!! El empleado se elimino con exito !!!\n',
	'empNoRegistrado':'\n El Empleado No se Encuentra Registrado en la Base de Datos\n',
	'elementNoPuedeSerEliminado1':'\nEl elemento encuentra prestado.No puede ser eliminado\n',
	'eliminacionElement1':'\nEl elemento tiene reservas, al eliminar el elemento estas se anularan\n',
	'eliminacionElementOk':'\n\n !!! El elemento se elimino con exito !!!\n',
	'elementNoRegistr':'\nElemento no registrado en la base de datos\n',
	'registroEmpOk':'\n !!! El empleado se registro con Exito !!!',
	'reserv1Ok':'\n El Elemento Reservado paso a Prestado con Exito',
	'elementNoDisponInventario':'\n Lo Sentimos, ya NO hay mas Elementos Disponibles en el Inventario.\n',
	'impHistorial1':'\n\n El Historial de Prestamos es:',
	'hoHayHistorial':'\n Aun no Existe Historial.',
	'LecturaDatosExitosa1':'\nDatos Leidos con Exito !!!',
	'noElementPrest':'\n Este Usuario No Tiene Elementos Prestados.',
	'estadoNoReconocido':'\n Estado no reconocido.',
	'userFullElement':'\n Este Empleado ya No Puede Prestar mas Elementos.',
	'estElementPrest':'\n Lo Sentimos el elemento se encuentra perestado.',
	'estElementReserv':'\n Lo Sentimos el Elemento se Encuentra Reservado.',
	'codNoEncotr':'\n Codigo No Encontrado en sus Elementos Prestados.',
	'elementDisp':'\n Los elementos disponibles son: ',
	'inventElement':'\n El inventario actual de elementos es: ',
	'elementPrest':'\n Los elementos prestados son: ',
	'noElementPres2':'\n No hay elementos prestados"',
	'elementRegistOk':'\n !!! Elemento Registrado con exito !!! ',
	'elementYaExite':' \n!!! Ya existe un elemento con este numero de codigo !!!',
	'userNoAutoriz':'El usuario no esta autorizado para realizar reservas!',
	'elementEncontradoOk':'\n Elemento Encontrado con Exito',
	'elementReservadoOk':'\n Elemento Reservado con exito',
	'elementNoEncontrado':'\n Elemento No Encontrado',
	'listElementReserv':'\n Sus elementos reservados son: ',
	'cancelarReservOk':'\n Reserva cancelada  con éxito',
	'elmentMasPrest':'El elemento mas prestado es: ',
	'ningunElementPrest':'\n Ningun elemento ha sido prestado',
	'5MasPrest':'\n Los 5 elementos mas prestados son: ',
	'ningunElementPrest2':'\n Aun no hay elemntos prestados',
	'registAdminAlmacen':'\n¿Empleado Administrador del almacen?\n\n1. Si.\n2. No.',
	'yaExistEmp':' \n!!! Ya existe un empleado con este numero de identificacion !!!\n',
	'empMasElementPrest':'\nEl empleado con mas elementos prestados es: ',
	'ningunPrestamo':'\nNingun empleado ha prestado elementos',
	'noHayValorPrest':'\n Aun no han sido prestado elementos con valor ',
	'baseDatEmpleados':'\nLa base de datos actual de empleados es: ',
	'empMasPrest':'El empleado que mas ha prestado elementos es: ',
	'rollMasPrest':'El roll que mas ha prestado elementos es: ',
	'optIn':'\nIngrese su Opcion: ',
	'emailIn':'\nIngrese su E-mail: ',
	'documentIn':'Ingrese su Documento: ',
	'userIn':'Ingrese su Usuario: ',
	'passwdIn':'Ingrese su Contraseña: ',
	'salirSoN':'\n Desea salir del sistema? (S/N): ',
	'continuar':'\n Presion Enter Para Continuar...',
	'finalizar':'\n\n Presione Enter Para Finalizar...',
	'idIn':'\n Ingrese la Identificacion del Usuario: ',
	'seguirEliminandoEmp':'\n¿Desea eliminar otro empleado?(s/n): ',
	'seguirEliminandoElement':'\n¿Desea eliminar otro elemento?(s/n): ',
	'seguirRegistEmp':'\n¿Desea registrar otro empleado?(s/n):  ',
	'setUser':'Establezca el usuario: ',
	'setPassd':'Establezca el password: ',
	'setIdAdmin':'Ingrese el id del Administrador: ',
	'setNomAdmin':'Ingrese el nombre del Administrador: ',
	'setApellAdmin':'Ingrese el apellido del Admnistrador: ',
	'setEmailAdmin':'Ingrese el correo del Administrador:',
	'setGradAdmin':'Establezca el grado del Administrador: ',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':''
	}

	@staticmethod
	def mostrarMensajes(msj):
		print(Mensaje().mensaje[msj])

	@staticmethod
	def mostrarBienvenidaPersonalizada(msj, emp):
		print(Mensaje().mensaje[msj] + str(emp.getNombre()) + " " + str(emp.getApellido()))

	@staticmethod
	def obtenerMensaje(msj):
		return Mensaje().mensaje[msj]