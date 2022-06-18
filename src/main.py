################
# Agustina Bover    @Agustina-Bover
# Manuel   Bernabei @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Programa principal, el esqueleto.
"""
from random import randint
try:
    import menu
    import misc.interfaz
    import misc.globales
except ImportError:
    import src.menu
    import src.misc.interfaz
    import src.misc.globales

class Error(Exception):
    """Clase base para otras excepciones."""

class ValorFueraDeRango(Error):
    """Cuando se ingresa un valor fuera del rango permitido."""

def ingreso_valor(minimo, maximo, operacion, mensaje):
    """Función que permite el ingreso de un valor en un intervalo definido."""
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(operacion)

    try:
        valor = float(input(mensaje))
        if not minimo <= valor <= maximo:
            raise ValorFueraDeRango
        if valor == 0:
            opciones()
    except ValorFueraDeRango:
        ingreso_valor(minimo, maximo, operacion, mensaje)

    return valor

def opciones():
    """Función que permite al usuario ver y elegir las distintas operaciones disponibles."""
    opcion = ingreso_valor(1, 4, 0, "\t\t\t\t Bienvenido\n\
\n\t\t  <1> Consulta <2> Retiro <3> Transferencia\n\t\t\t\t  <4> Salir\
\n\n>> Ingrese número de operación: ")

    codigo = menu.operacion(opcion)

    if 2 <= opcion <= 3:
        if 0 < codigo < 3:
            print("\t\t\t      Operación exitosa")
            if codigo == 2:
                print("\t\t\t\t Imprimiendo")
        else:
            print("\t\t    Operación fallida, cuenta inexistente")

        misc.globales.lapso()
        opciones()

def ingreso():
    """Función que solicita el ingreso de los datos del usuario para verificar su identidad."""
    clave     = ingreso_valor(10000, 99999, 1, ">> Ingrese la clave de seguridad: ")
    documento = ingreso_valor(10000000, 99999999, 1, ">> Ingrese su nro. de documento : ")

    return menu.inicio(clave, documento)

def generacion_movimientos():
    """Función que genera 10 movimientos aleatorios."""
    nombres  = ("Depósito     ", "Extracción   ", "Recibo       ", "Transferencia")

    if misc.globales.bandera is False:
        misc.globales.bandera = True

        for _ in range(10):
            i = randint(0, 3)
            j = randint(0, 1)
            if j == 1:
                valores = (randint(1, 15) * 550) * 1.2   # ARS
                misc.globales.mov_monedas.append("ARS")
            else:
                valores = (randint(1, 15) * 22.05) * 1.2 # PER
                misc.globales.mov_monedas.append("PER")

            misc.globales.mov_nombres.append(nombres[i])
            misc.globales.mov_valores.append(round(valores, 2))

def principal():
    """Función que permite el inicio de tus aventuras con la ATM."""
    misc.interfaz.activacion()

    intentos, usuario_validado = 0, False

    generacion_movimientos()

    while usuario_validado is not True:
        misc.interfaz.head()

        intentos += 1
        usuario_validado = ingreso()
        if intentos == 3:
            misc.interfaz.final(1)

    opciones()

if __name__ == "__main__":
    principal()
