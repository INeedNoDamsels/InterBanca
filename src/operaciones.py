"""
Operaciones varias.
"""

from misc.globales import tipo_cambio

def transferencia(): # Manu.
    """
    Función que permite la ejecución de la operación de transferencias.
    """
    opcion = int(input("\n\t\t\t\t[TRANSFERENCIA]\n\n \
>> Ingrese número de cuenta destino: "))
    try:
        assert opcion == 98765
        tipo_cambio()

    except:
        pass
