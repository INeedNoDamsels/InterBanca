"""
Operaciones disponibles del ATM.
"""
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

def movimientos():
    """
    Función que muestra los movimientos realizados por el usuario.
    """
    for i in range(len(misc.globales.mov_nombres)):
        print(f"\t\t\t ---------------------------\n\t\t\t\
{misc.globales.mov_nombres[i]} {misc.globales.mov_monedas[i]} ${misc.globales.mov_valores[i]}")

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
    Función que permite la consulta de información de la cuenta.
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

    if (menu.validar_datos(clave, misc.globales.clave_a)) is True:
        if pregunta == 1:
            codigo = 2
        else:
            codigo = 1
        if misc.globales.moneda == "ARS":
            misc.globales.dinero -= monto
        else:
            misc.globales.dinero -= misc.globales.conversor_a_ars(monto)
        misc.globales.mov_nombres.append("Extracción   ")
        misc.globales.mov_valores.append(round(monto, 2))
        misc.globales.mov_monedas.append(misc.globales.moneda)
    else:
        codigo = 0

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
        misc.globales.mov_monedas.append(misc.globales.moneda)
        codigo = 1
    else:
        codigo = 0

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
