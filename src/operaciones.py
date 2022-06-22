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

def consulta(opcion, moneda, saldo):
    """
    Función que permite la consulta de información de la cuenta.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(3)

    if opcion == 1:
        print(f"\t\t\tSaldo disponible: ${saldo} {moneda}")
    elif opcion == 2:
        for i in range(len(main.mov_nombres)): # cambiar
            print(f"\t\t\t ---------------------------\n\t\t\t\
  {main.mov_nombres[i]} {main.mov_monedas[i]} ${main.mov_valores[i]}") # cambiar

    misc.interfaz.continuar()
    main.opciones()

def retiro(clave, monto, pregunta, moneda):
    """
    Función que permite el retiro de dinero.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(4)

    if (menu.validar_datos(clave, 12345)) is True:
        if pregunta == 1:
            codigo = 2
        else:
            codigo = 1
        if moneda == "ARS":
            misc.globales.dinero -= monto # cambiar
        else:
            misc.globales.dinero -= misc.globales.conversor_a_ars(monto) # cambiar
        main.mov_nombres.append("Extracción   ") # cambiar
        main.mov_valores.append(round(monto, 2)) # cambiar
        main.mov_monedas.append(moneda) # cambiar
    else:
        codigo = 0

    return codigo

def transferencia(clave, monto, moneda):
    """
    Función que permite la transferencia de dinero de una cuente a otra.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(5)

    if menu.validar_datos(clave, 98765) is True:
        if moneda == "ARS":
            misc.globales.dinero -= monto # cambiar
        else:
            misc.globales.dinero -= misc.globales.conversor_a_ars(monto) # cambiar
        main.mov_nombres.append("Transferencia") # cambiar
        main.mov_valores.append(round(monto, 2)) # cambiar
        main.mov_monedas.append(moneda) # cambiar
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
