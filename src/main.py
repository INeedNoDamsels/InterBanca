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

def ingreso_valor(minimo, maximo, operacion, mensaje, movimientos):
    """Función que permite el ingreso de un valor en un intervalo definido."""
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(operacion)

    try:
        valor = float(input(mensaje))
        if not minimo <= valor <= maximo:
            raise ValorFueraDeRango
        if valor == 0:
            opciones(movimientos)
    except ValorFueraDeRango:
        ingreso_valor(minimo, maximo, operacion, mensaje, movimientos)
    except ValueError:
        valor = None
        ingreso_valor(minimo, maximo, operacion, mensaje, movimientos)

    return valor

def opciones(movimientos):
    """Función que permite al usuario ver y elegir las distintas operaciones disponibles."""
    opcion = ingreso_valor(1, 4, 0, "\t\t\t\t Bienvenido\n\
\n\t\t  <1> Consulta <2> Retiro <3> Transferencia\n\t\t\t\t  <4> Salir\
\n\n>> Ingrese número de operación: ", movimientos)

    codigo = menu.operacion(opcion, movimientos)

    if 2 <= opcion <= 3:
        if 0 < codigo < 3:
            print("\t\t\t      Operación exitosa")
            if codigo == 2:
                print("\t\t\t\t Imprimiendo")
        else:
            print("\t\t    Operación fallida, cuenta inexistente")

        misc.globales.lapso()
        opciones(movimientos)

def ingreso(movimientos):
    """Función que solicita el ingreso de los datos del usuario para verificar su identidad."""
    clave     = ingreso_valor(10000, 99999, 1, ">> Ingrese la clave de seguridad: ", movimientos)
    documento = ingreso_valor(10000000, 99999999, 1, ">> Ingrese su nro. de documento : ", movimientos)

    return menu.inicio(clave, documento)

def generacion_movimientos(bandera):
    """Función que genera 10 movimientos aleatorios."""
    mov_nombres, mov_valores, mov_monedas = [], [], []
    nombres  = ("Depósito     ", "Extracción   ", "Recibo       ", "Transferencia")

    if bandera is False:
        bandera = True

        for _ in range(10):
            i = randint(0, 3)
            j = randint(0, 1)
            if j == 1:
                valores = (randint(1, 15) * 550) * 1.2   # ARS
                mov_monedas.append("ARS")
            else:
                valores = (randint(1, 15) * 22.05) * 1.2 # PER
                mov_monedas.append("PER")

            mov_nombres.append(nombres[i])
            mov_valores.append(round(valores, 2))

    return (mov_nombres, mov_valores, mov_monedas)

def principal():
    """Función que permite el inicio de tus aventuras con la ATM."""
    misc.interfaz.activacion()

    bandera = False
    intentos, usuario_validado = 0, False

    movimientos = generacion_movimientos(bandera)

    while usuario_validado is not True:
        misc.interfaz.head()

        intentos += 1
        usuario_validado = ingreso(movimientos)
        if intentos == 3:
            misc.interfaz.final(1)

    opciones(movimientos)

if __name__ == "__main__":

    principal()
