"""
Operaciones disponibles del ATM.
"""
import menu
import misc.interfaz
from misc.globales import tipo_cambio, lapso

def consulta(): # Ambos.
    """
    Función que permite la consulta de saldo en la cuenta.
    """
    misc.interfaz.head()

    misc.interfaz.nombre_operacion(0)
    opcion = int(input("\t\t     <1> Posición global <2> Movimientos\n\t\t\t\t  <3> Salir \
\n >> Ingrese operación: "))

    if opcion == 1:
        misc.globales.tipo_cambio()
        misc.interfaz.head()
        misc.interfaz.nombre_operacion(0)
        print(f"\t\t\tSaldo disponible: ${misc.globales.saldo} {misc.globales.moneda}")
        misc.interfaz.continuar()
    elif opcion == 2:
        pass # Movimientos
    else:
        menu.opciones()

    menu.opciones()

def retiro(): # Agus.
    """
    Función que permite el retiro de dinero.
    """
    misc.interfaz.head()

    misc.interfaz.nombre_operacion(1)

def transferencia():
    """
    Función que permite la transferencia de dinero de una cuente a otra.
    """
    misc.interfaz.head()

    misc.interfaz.nombre_operacion(2)
    numero = int(input(" >> Ingrese número de cuenta destino: "))

    try:
        assert numero == misc.globales.clave_b
        tipo_cambio()

        monto = float(input("\n >> Ingrese monto: $"))
        try:
            assert 0 < monto <= misc.globales.saldo
            if misc.globales.moneda == "ARS":
                misc.globales.dinero -= monto
            else:
                misc.globales.dinero -= misc.globales.conversor_a_ars(monto)

            misc.interfaz.head()
            misc.interfaz.nombre_operacion(2)
            print("\t\t\t      Operación exitosa")
        except:
            misc.interfaz.head()
            misc.interfaz.nombre_operacion(2)
            print("\t\t\t     Saldo insuficiente")
    except:
        misc.interfaz.head()
        misc.interfaz.nombre_operacion(2)
        print("\t\t\t     Cuenta inexistente")

    lapso(3)
    menu.opciones()

def salir():
    """
    Función que permite la salida voluntaria del usuario.
    """
    misc.interfaz.head()

    misc.interfaz.nombre_operacion(3)
    print("\t\t\t     Expulsando tarjeta")
    lapso(3)

    misc.interfaz.final("\n\t\t\t      Guarde su tarjeta \
\n\t\t     Gracias por confiar en InterBanca ©")
