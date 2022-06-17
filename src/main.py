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
        if valor == -1:
            opciones()
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
\n\t\t  <1> Consulta <2> Retiro <3> Transferencia\n\t\t\t\t  <4> Salir\
\n\n>> Ingrese número de operación: ")

    codigo = menu.operacion(opcion)

    if 2 <= opcion <= 3:
        if codigo == 0:
            print("\t\t\t      Operación exitosa")
        elif codigo == 2:
            print("\t\t\t      Operación exitosa\n\t\t\t\t Imprimiendo")
        else:
            print("\t\t\t      Operación fallida")

        misc.globales.lapso()
        opciones()

def ingreso():
    """
    Función que solicita el ingreso de los datos del usuario para verificar su identidad.
    """
    clave = ingreso_valor(0, 99999, 1, ">> Ingrese la clave de seguridad: ")
    documento = ingreso_valor(0, 99999999, 1, ">> Ingrese su nro. de documento : ")

    return menu.inicio(clave, documento)

def principal():
    """
    Función que permite el inicio de tus aventuras con la ATM.
    """
    misc.interfaz.activacion()

    intentos, usuario_validado = 0, False

    while usuario_validado is not True:
        misc.interfaz.head()

        intentos += 1
        usuario_validado = ingreso()        
        if intentos == 2:
            misc.interfaz.final(1)

    opciones()

if __name__ == "__main__":
    principal()
