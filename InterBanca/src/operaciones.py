"""
Operaciones varias.
"""

from src.misc.globales import *

def consulta(): # Continuar juntos.

    monto, moneda = tipo_cambio(int(input("\n >> Ingrese tipo de moneda (<1> AR$, <2> PER): ")))

    opcion = int(input("\n\t\t <1> Posicionamiento global <2> Movimientos\n\t\t\t\t  <3> Salir\n \
Ingrese operación: "))

    if opcion == 1:
        print(f"Saldo: {monto} {moneda}")
    else:
        pass

def retiros(): # Agus.
    """
    """
    pass

def transferencia(): # Manu.
    """
    """
    pass

def salir(): # Juntos (?)
    """
    """
    pass
