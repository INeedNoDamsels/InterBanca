################
# Agustina Bover    @Agustina-Bover
# Manuel   Bernabei @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Programa principal, el esqueleto.
"""
try:
    import menu
    import misc.interfaz
    import misc.globales
except ImportError:
    import src.menu
    import src.misc.interfaz
    import src.misc.globales

class Error(Exception):
    """
    Clase base para otras excepciones.
    """

class ValorFueraDeRango(Error):
    """
    Cuando se ingresa un valor fuera del rango permitido.
    """

def ingreso_valor(minimo, maximo, operacion, mensaje):
    """
    Función que permite el ingreso de un valor en un intervalo definido.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(operacion)

    try:
        valor = int(input(mensaje))
        if not minimo <= valor <= maximo:
            raise ValorFueraDeRango
    except ValorFueraDeRango:
        ingreso_valor(minimo, maximo, operacion, mensaje)

    return valor

def opciones():
    """
    Función que permite al usuario ver y elegir las distintas operaciones disponibles.
    """
    opcion = ingreso_valor(1, 4, 0, "\t\t\t\t Bienvenido\n\
\n\t\t  <1> Consulta <3> Retiro <3> Transferencia\n\t\t\t\t  <4> Salir\
\n\n>> Ingrese número de operación: ")

    menu.operacion(opcion)

def ingreso():
    """
    Función que solicita el ingreso de los datos del usuario para verificar su identidad.
    """
    clave = ingreso_valor(0, 99999, 1, ">> Ingrese la clave de seguridad: ")
    documento = ingreso_valor(0, 999999999, 1, ">> Ingrese su nro. de documento : ")

    return menu.inicio(clave, documento)

def principal():
    """
    Función que permite el inicio de tus aventuras con la ATM.
    """
    intentos, usuario_validado = 0, False
    misc.interfaz.activacion()

    while usuario_validado is not True:
        misc.interfaz.head()
        intentos += 1
        usuario_validado = ingreso()

        if intentos == 3:
            misc.interfaz.final(1)

    opciones()

if __name__ == "__main__":
    principal()
