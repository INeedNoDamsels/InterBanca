"""
Menú de opciones.
"""

from misc.ASCII import head

def opciones():
    """
    Función que imprime las opciones disponibles.
    """
    head()

    opcion = int(input("\n<1> Consultas\n<2> Retiros\n<3> Transferencia\n<4> Salir\n\t  >> Ingrese operación: "))
    
    try:
        operacion(opcion)
        assert opcion > 0 and opcion < 5
    except:
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
