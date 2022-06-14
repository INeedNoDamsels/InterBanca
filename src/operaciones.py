"""
Operaciones disponibles del ATM.
"""
try:
    import main
    import menu
    import misc.interfaz
except ImportError:
    import src.main
    import src.menu
    import src.misc.interfaz

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

def consulta(opcion):
    """
    Función que permite la consulta de saldo en la cuenta.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(3)

    if opcion == 1:
        print(f"\t\t\tSaldo disponible: ${misc.globales.saldo} {misc.globales.moneda}")
        misc.interfaz.continuar()
    elif opcion == 2:
        pass # Movimientos

    main.opciones()

def retiro():
    """
    Función que permite el retiro de dinero.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(4)

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
