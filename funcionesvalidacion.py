import re
from random import randint
#from administradoralmacen import AdministradorAlmacen
#from importacion1 import Empleado, Administrativo

# Página de referencia: https://parzibyte.me/blog/2018/12/04/comprobar-correo-electronico-python/
def comprobarCorreoValido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

"""
def comprobarExistenciaCorreo(empleados, email):
    for emp in empleados:
        if emp.getEmail() == email:
            return True
    return False


def generarUsuario(empleados, email):
    correo1 = email.upper()
    separacion = correo1.split('@')
    usuario = separacion[0]
    
    while verificarUsuario(empleados, usuario):
        usuario = generarNuevoUsuario(usuario)
    return usuario


def verificarUsuario(empleados, usuario):
    for emp in empleados:
        if isinstance(emp, AdministradorAlmacen):
            if emp.getUsuario() == usuario:
                return True
    return False


def generarNuevoUsuario(usuario):
    complemento = str(randint(1, 800))
    user = usuario + complemento
    return user
"""