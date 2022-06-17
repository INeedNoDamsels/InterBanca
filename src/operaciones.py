"""
Operaciones disponibles del ATM.
"""
from random import randint
try:
    import main
    import menu
    import misc.interfaz
    import misc.globales
except ImportError:
    import src.main
    import src.menu
    import src.misc.interfaz
    import src.misc.globales

def configuracion():
    """
    Función que habilita o deshabilita el paso del tiempo al ejecutar ciertas operaciones.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(2)

    opcion = input("¿Habilitar acciones con tiempo? (s/n): ")
    if opcion in ("s", "S"):
        misc.globales.tiempos = True
    elif opcion in ("n", "N"):
        misc.globales.tiempos = False
    else:
        configuracion()

def movimientos():
    """
    """
    nombres  = ("Depósito     ", "Extracción   ", "Recibo       ", "Transferencia")

    if misc.globales.ejecutado is False:

        misc.globales.ejecutado = True

        for _ in range(10):
            valores = (randint(1, 15) * 550) * 1.2

            if misc.globales.moneda == "PER":
                valores = misc.globales.conversor_a_per(valores)

            i = randint(0, 3)
            misc.globales.mov_nombres.append(nombres[i])
            misc.globales.mov_valores.append(round(valores, 2))

    for j in range(len(misc.globales.mov_nombres)):
        print(f"\t\t\t   -----------------------\
\n\t\t\t    {misc.globales.mov_nombres[j]} ${misc.globales.mov_valores[j]}")

def consulta(opcion):
    """
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(3)

    if opcion == 1:
        print(f"\t\t\tSaldo disponible: ${misc.globales.saldo} {misc.globales.moneda}")
    elif opcion == 2:
        movimientos()

    misc.interfaz.continuar()
    main.opciones()

def retiro(clave, monto, pregunta):
    """
    Función que permite el retiro de dinero.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(4)

    if menu.validar_datos(clave, misc.globales.clave_a) is True:
        if pregunta == 1:
            codigo = 2
        else:
            codigo = 0
        if misc.globales.moneda == "ARS":
            misc.globales.dinero -= monto
        else:
            misc.globales.dinero -= misc.globales.conversor_a_ars(monto)
        misc.globales.mov_nombres.append("Extracción   ")
        misc.globales.mov_valores.append(round(monto, 2))
    else:
        codigo = 1

    return codigo

def transferencia(clave, monto):
    """
    Función que permite la transferencia de dinero de una cuente a otra.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(5)

    if menu.validar_datos(clave, misc.globales.clave_b) is True:
        if misc.globales.moneda == "ARS":
            misc.globales.dinero -= monto
        else:
            misc.globales.dinero -= misc.globales.conversor_a_ars(monto)
        misc.globales.mov_nombres.append("Transferencia")
        misc.globales.mov_valores.append(round(monto, 2))
        codigo = 0
    else:
        codigo = 1

    return codigo

def salir():
    """
    Función que permite la salida voluntaria del usuario.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(6)

    print("\t\t\t     Expulsando tarjeta")
    misc.globales.lapso()

    misc.interfaz.final(0)
