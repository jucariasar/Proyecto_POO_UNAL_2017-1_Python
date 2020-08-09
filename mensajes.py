

class Mensaje():
	mensaje = {
	'menuPpal':' 1. Ingresar al Sistema.\n 2. Consultar Inventario de Elementos.\n 3. Ingresar Como Super Usuario.\n 4. Salir.',
	'optIn':'\n Ingrese su Opcion: ',
	'optInvalid':'\n\n\t¡¡¡ Opcion Invalida !!!',
	'inventElement':'El inventario actual de elementos es: ',
	'correoInvalido':'\n\n\t¡¡¡ Formato de Correo Invalido !!!', 
	'intentarNuevo':'\n Por Favor Intente Nuevamente',
	'emailIn':'\n\n Ingrese el E-mail: ',
	'documentIn':' Ingrese el Documento: ',
	'emailDocumentInvalid':'\n\n\t¡¡¡ E-mail y/o Documento Invalido !!!\n',
	'volverAnterior':' ¿Volver al Menu Principal? S/N',
	'bienvenida':' \n\n Bienvenid@ ',
	'menuEmpleado':' ¿Que desea hacer?\n\n 1. Consultar Elementos Disponibles.\n 2. Consultar Elementos Prestados.\n 3. Reservar Elementos para Prestar.\n 4. Modificar Reserva de Elementos.\n 5. Cerrar Sesion de Usuario.',
	'SelectRollAdmin':'\n\n Con que Roll Desea Ingresar:\n\n 1. Como Administrador del Almacen.\n 2. Como Empleado NO Administrador.\n 3. Desea volver al menu principal.',
	'infoAdmin1':'\n A continuacion debe de ingresar su usuario y contraseña para ingresar a administrar la aplicacion',
	'userIn':'\n Ingrese el Usuario: ',
	'passwdIn':' Ingrese la Contraseña: ',
	'userPassInvalid':'\n Usuario y/o Contraseña Incorrecto.',
	'menuPpalAdmin':'\n\n Menu de Usuario Administrador del Almacen:\n\n 1. Ir al Menu de Consultas.\n 2. Ir al Menu de Registros / Borrados.\n 3. Prestar / Recibir.\n 4. Cerrar Sesion de Administrador.',
	'menu1Admin':'\n\n ¿Que Consulta Desea Realizar?\n\n 1. Consultar Inventario de Elementos.\n 2. Consultar Base de Datos de Empleados.\n 3. Consultar el Elemento mas Prestado.\n 4. Consultar los 5 Elementos mas Prestados.\n 5. Consultar Empleado con mas Elementos Prestados.\n 6. Consultar Empleados con mas Valor Prestado.\n 7. Consultar el Empleado que mas Presta.\n 8. Consultar el Roll que mas Presta.\n 9. Volver al Menu Anterior.',
	'menu2Admin':'\n\n ¿Que desea hacer?\n\n 1. Registrar Empleado.\n 2. Registrar Elemento.\n 3. Eliminar Empleado.\n 4. Eliminar Elemento.\n 5. Volver al Menu Anterior.',
	'registEmp1':'\n\n ¿Qué tipo de empleado desea registrar?\n\n 1.Empleado Administrativo.\n 2.Empleado Operario.\n 3.Ingeniero Tecnico.\n 4.Regresar al Menu anterior',
	'registAdminAlmacen':'\n\n ¿Empleado Administrador del almacen?\n\n 1. Si.\n 2. No.\n 3. Volver.',
	'yaExistEmp':' \n!!! Ya existe un empleado con este numero de identificacion !!!\n',
	'setUser':' \n\n Establezca el usuario: ',
	'setPassd':' Establezca el password: ',
	'setIdAdmin':' Ingrese el id del Administrador: ',
	'setNomAdmin':' Ingrese el nombre del Administrador: ',
	'setApellAdmin':' Ingrese el apellido del Admnistrador: ',
	'setEmailAdmin':' Ingrese el correo del Administrador:',
	'setGradAdmin':' Establezca el grado del Administrador: ', # Mensajes
	'replayEmail':' Email en uso por otro usuario.',
	'emailAsign':' Email asignado: ',
	'userAsign':' Usuario asignado: ',
	'invalidDocument':' El documento debe ser un dato numerico',
	'menu3Admin':'\n\n ¿Que desea hacer?:\n\n 1. Prestar Elementos.\n 2. Recibir Elementos.\n 3. Mostrar Historial.\n 4. Volver al Menu Anterior.',
	'menu3Opt1':'\n El usuario actualmente tiene elemento(s) reservado(s): \n\n ¿Que Desea Hacer?:\n\n 1. Asentar la reserva.\n 2. Prestar nuevos elementos.\n 3. Volver.',
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
	'elementPrest':'\n Los elementos prestados son: ',
	'noElementPres2':'\n No hay elementos prestados.',
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
	'empMasElementPrest':'\nEl empleado con mas elementos prestados es: ',
	'ningunPrestamo':'\nNingun empleado ha prestado elementos',
	'noHayValorPrest':'\n Aun no han sido prestado elementos con valor ',
	'baseDatEmpleados':'\nLa base de datos actual de empleados es: ',
	'empMasPrest':'El empleado que mas ha prestado elementos es: ',
	'rollMasPrest':'El roll que mas ha prestado elementos es: ',
	'salirSoN':'\n Desea salir del sistema? (S/N): ',
	'continuar':'\n Presion Enter Para Continuar...',
	'finalizar':'\n\n Presione Enter Para Finalizar...',
	'idIn':'\n Ingrese la Identificacion del Usuario: ',
	'seguirEliminandoEmp':'\n¿Desea eliminar otro empleado?(s/n): ',
	'seguirEliminandoElement':'\n¿Desea eliminar otro elemento?(s/n): ',
	'seguirRegistEmp':'\n¿Desea registrar otro empleado?(s/n):  ',
	'elementToWrite':'Numero de elementos que desea escribir: ',
	'codElementAPrestar':'\n Ingrese el codigo del elemento a prestar: ',
	'presMasElementSoN':'\n Desea Prestar mas Elementos? (S/N): ',
	'codElementAEntre':'\n Ingrese el codigo del elementos que va a entregar: ',
	'entreMasElementosSoN':'\n Desea seguir entregando? (S/N): ',
	'codElementRegist':'\nIngrese codigo del elemento: ',
	'setNomElement':'Ingrese nombre del elemento: ',
	'setUbiElement':'Ingrese la ubicacion del elemento: ',
	'setValorElement':'Ingrese valor economico del elemento: ',
	'seguirRegistElement':'\n¿Desea registrar otro elemento?(s/n): ',
	'elementAReserv':'\n Ingrese codigo del elemento que desea reservar: ',
	'reservarSoN':'\n Desea Reservar?  (S/N): ',
	'codModReserv':'\n Ingrese codigo del elemento al cual desea modificar la reserva: ',
	'modReservSoN':'\n Desea Cancelar Reservar?  (S/N): ',
	'setIdIng':'Ingrese el id del ingeniero: ',
	'setNomIng':'Ingrese el nombre del ingeniero: ',
	'setApellIng':'Ingrese el apellido del ingeniero: ',
	'setEmailIng':'Ingrese el correo del ingeniero: ',
	'setAreaIng':'Establezca area del Ingeniero: ',
	'setIdOp':'\nIngrese el id del operario: ',
	'setNomOp':'Ingrese el nombre del operario: ',
	'setApellOp':'Ingrese el apellido del operario: ',
	'setEmailOp':'Ingrese el correo del operario: ',
	'setTipo':'Establezca el tipo de operario: '
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

	@staticmethod
	def mostrarEmail(msj, email):
		print(Mensaje().mensaje[msj] + email)


	@staticmethod
	def mostrarUsuarioAsignado(msj, usuario):
		print(Mensaje().mensaje[msj] + usuario)