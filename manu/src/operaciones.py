"""
Operaciones disponibles del ATM.
"""
import menu
import misc.interfaz
from misc.globales import tipo_cambio, lapso

def consulta(): # Ambos.
    """
    """
    misc.interfaz.head()

    opcion = int(input("\n\t\t\t\t[  CONSULTAS  ]\n\n \
\t\t     <1> Posición global <2> Movimientos\n\t\t\t\t  <3> Salir \
\n >> Ingrese operación: "))

    if opcion == 1:
        tipo_cambio()
        print(f"\n\t\t Saldo disponible: ${misc.globales.saldo} {misc.globales.moneda}")

    lapso(3)
    menu.opciones()

def retiro(): # Agus.
    """
    """
    pass

def transferencia(): # Manu.
    """
    Función que permite la transferencia de dinero de una cuente a otra.
    """
    misc.interfaz.head()

    numero = int(input("\n\t\t\t\t[TRANSFERENCIA]\n\n \
>> Ingrese número de cuenta destino: "))

    try:
        assert numero == misc.globales.clave_b
        tipo_cambio()
        monto = float(input(f"\n >> Ingrese monto: $"))
        if misc.globales.moneda == "PER":
            monto = misc.globales.conversor(monto)

        try:
            assert monto <= misc.globales.saldo
            misc.interfaz.head()

            if misc.globales.moneda == "PER":
                monto -= conversor(misc.globales.saldo_ar)
            else:
                monto -= misc.globales.saldo_ar
            print("\n\t\t\t      Operación exitosa")
        except:
            print("\n\t\t\t     Saldo insuficiente")

    except:
        misc.interfaz.head()
        print("\n\t\t\t     Cuenta inexistente")

    lapso(5)
    menu.opciones()

def salir():
    """
    Función que permite la salida voluntaria del usuario.
    """
    misc.interfaz.head()

    print("\n\t\t\t   Expulsando tarjeta")
    lapso(3)

    misc.interfaz.final("\n\t\t\t      Guarde su tarjeta \
\n\t\t     Gracias por confiar en InterBanca ©")