"""
Menú de opciones.
"""

import os
from src.misc.ascii import head
from src.operaciones import *

def opciones(): # Aca no hace falta agregar nada ;)
    """
    Función que imprime las opciones disponibles.
    """
    head()

    opcion = int(input("\n\t\t <1> Consultas <2> Retiros <3> Transferencia\n \
\t\t\t\t  <4> Salir\n \
>> Ingrese operación: "))

    try:
        assert 0 < opcion < 5
        operacion(opcion)
    except:
        os.system('cls') # Solo para S.O. Windows.
        opciones()

def operacion(opcion): # Agregar condicional y llamar funcion correspondiente a 'opcion'.
    """
    Función que determina la operación ingresada.
    """
    if opcion == 1:
        consulta()
    else:
        pass
