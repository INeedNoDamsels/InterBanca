"""
Menú de opciones.
"""

from misc.ASCII import head

def opciones():
    """
    Función que imprime las opciones disponibles.
    """
    head()

    opcion = int(input("\n\t\t\t  <1> Consultas <2> Retiros <3> Transferencia\n \
\t\t\t\t\t   <4> Salir\n \
>> Ingrese operación: "))

    try:
        operacion(opcion)
        assert opcion > 0 and opcion < 5
    except:
        # estaría bueno limpiar la pantalla en este punto, ¿import os; os.system('cls')?
        opciones()

def operacion(numero):
    """
    Función que determina la operación ingresada.
    """

    if numero == 1:
        print("Uno")
    elif numero == 2:
        print("Dos")
    elif numero == 3:
        print("Tres")
    elif numero == 4:
        print("Cuatro")
