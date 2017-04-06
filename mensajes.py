from empleado import Empleado
from administradoralmacen import AdministradorAlmacen
from administrativo import Administrativo
from ingenierotecnico import IngenieroTecnico
from operario import Operario

class Mensaje():
	mensaje = {
	'bienvenida':'\n\nBienvenido ',
	'optInvalid':'\n ¡¡¡ Opcion Invalida !!!',
	'menuPpal':'\n\n1. Crear Datos Ficticios.\n2. Crear Datos Ficiticos Desde un txt.\n3. Ingresar al Sistema.\n4. Salir',
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
	'empNoRegistrado':'\nEmpleado no registrado en la base de datos\n',
	'elementNoPuedeSerEliminado1':'\nEl elemento encuentra prestado.No puede ser eliminado\n',
	'eliminacionElement1':'\nEl elemento tiene reservas, al eliminar el elemento estas se anularan\n',
	'eliminacionElementOk':'\n\n !!! El elemento se elimino con exito !!!\n',
	'elementNoRegistr':'\nElemento no registrado en la base de datos\n',
	'registroEmpOk':'\n !!! El empleado se registro con extito !!!',
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