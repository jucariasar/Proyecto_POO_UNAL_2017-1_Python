# Proyecto_POO_UNAL_2017-1_Python
Proyecto del grupo 7 para la materia POO en la UNAL sede Medellín 2017-1

Con este proyecto se quiere dar solución al problema planteado a continuación:


Sistematización del proceso de almacenamiento y préstamo de elementos.

La empresa Metalmecánica SAS se encarga de fabricar elementos metalmecánicos para utilizar en industrias y hogares; la empresa cuenta con un almacén (bodega) en su interior destinado al almacenamiento de elementos de consumo y devolutivos que son requeridos por los diferentes empleados de la empresa para realizar actividades administrativas y de mantenimiento. Los empleados de la empresa están divididos en 3 grupos, empleados administrativos, empleados ingenieros técnicos, y empleados operarios; hasta el momento los préstamos en el almacén se debían realizar mediante formatos físicos en los cuales las personas encargadas del almacén anotaban los elementos que cada empleado prestaba. La empresa en una campaña ambiental y de oficinas sin papel, ha decidido sistematizar el proceso de préstamos en su almacén, para ello la empresa requiere que se le realice una aplicación para controlar la gestión de los préstamos con las siguientes condiciones:

1.	La aplicación debe permitir a los usuarios administradores de la aplicación registrar y borrar tanto empleados como elementos en las diferentes bases de datos para empleados y elementos. Cuando un empleados es registrado, deben de quedar habilitado para realizar préstamos; además un empleado no puede ser borrado de la base de datos si tiene elementos prestados; igualmente los elementos registrados quedaran habilitados para ser prestados por los diferentes empleados, además un elemento no puede ser borrado si se encuentra prestado a algún empleado.
2.	Tanto empleados administrativos, ingenieros técnicos y operarios pueden realizar prestamos en el almacén, siguiendo las siguientes condiciones:
2.1.	Los empleados administrativos pueden prestar hasta un máximo de 5 elementos.
2.2.	Los empleados ingenieros técnicos pueden prestar hasta un máximo de 10 elementos.
2.3.	Los empleados operarios pueden prestar hasta un máximo de 15 elementos.

3.	Dado que el objetivo principal de la aplicación es registrar, borrar y consultar elementos a empleados de una manera eficiente y rápida, la interface de los usuarios administradores de la aplicación debe de tener la opción para prestar, borrar o consultar elementos de un empleado.

4.	Todos los empleados registrados en la aplicación pueden realizar consultas de los elementos en la base de datos, además pueden reservar uno o varios elementos logiandose mediante su número de documento y el correo electrónico; igualmente pueden cancelar elementos previamente reservados por ellos si así lo desean. 

5.	La aplicación principal será administrada por 3 usuarios administrativos en 3 turnos de trabajo (mañana, tarde y noche) encargados del control de los inventarios del almacén, dichos usuarios aunque son administrativos, cuenta además con un nombre de usuario y contraseña, mediante los cuales pueden acceder a administrar la aplicación del almacén.

6.	Para un buen control del inventario por parte de los usuarios administradores de la aplicación, esta debe de tener las opciones: listar todos elementos del inventario del almacén, y listar todos los usuarios registrados en la base de datos; igualmente se debe de poder consultar los elementos más prestados y los empleados con más elementos y valor prestado.

7.	Que un elementos se encuentre reservado no significa que ya se encuentra prestado, pero no debe de estar disponible para que otro empleado diferente al que lo reservo lo reserve o lo preste, además solo los usuarios con el rol de administradores de la aplicación podrán asentar el préstamo cuando el empleado se desplace personalmente por el elemento reservado. 

En la aplicación se deben registrar todos los elementos que pertenecen al inventario de la empresa; cabe resaltar que en el inventario, cada elemento tiene un código único que lo identifica, un nombre y la ubicación. La ubicación es un código que informa al administrador del almacén en que estantería de la bodega se encuentra ubicado el elemento.
