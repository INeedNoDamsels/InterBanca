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
    import src.misc.globales
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
def movimientos():
    textos  = ( "Extracción de $", "Transferencia de $", "Recibo de $", "Depósito de $")
    x=[]
    y=[]
    if misc.globales.ejecutado is False:
        for i in range(10):
            misc.globales.ejecutado=True
            valores = randint(1, 15) * 550
            x.append (randint(0, 3))
            if misc.globales.moneda=="PER":
                valores=misc.globales.conversor_a_per(valores)
            y.append(valores)
    for j in range(10):
        contador=x[j]
        print(f"{textos[contador]}{y[contador]}")

def consulta(opcion):
    if opcion == 1:
        print(f"\t\t\tSaldo disponible: ${misc.globales.saldo} {misc.globales.moneda}")
    elif opcion ==2:
        movimientos()
        misc.interfaz.continuar()
    main.opciones()

def retiro(clave,monto,pregunta):
    """
    Función que permite el retiro de dinero.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(4)
    if menu.validar_datos(clave, misc.globales.clave_a) is True:
        if pregunta==1:
            codigo=2
        else:
            codigo=0
        if misc.globales.moneda == "ARS":
            misc.globales.dinero -= monto
        else:
            misc.globales.dinero -= misc.globales.conversor_a_ars(monto)
    else:
        codigo=1
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
