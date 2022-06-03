"""
Menú de opciones.
"""
from misc.interfaz import head
from misc.globales import lapso
from operaciones   import transferencia

def activacion():
    """
    Función que simula la inicialización del ATM, el ingreso y lectura de la tarjeta.
    """
    head()
    input("\n\t\t\tPresione Enter para continuar")

    head()
    print("\n\t\t       Ingrese la tarjeta en la ranura")
    lapso()

    head()
    print("\n\t\t\t     Leyendo tarjeta")
    lapso()

    opciones()

def opciones(): # Aca no hace falta agregar nada ;)
    """
    Función que imprime las opciones disponibles.
    """
    head()

    opcion = int(input("\n\t\t <1> Consultas <2> Retiros <3> Transferencia\n \
\t\t\t\t  <4> Salir\n >> Ingrese operación: "))

    try:
        assert 0 < opcion < 5
        operacion(opcion)
    except:
        opciones()

def operacion(opcion): # Agregar condicional y llamar función correspondiente.
    """
    Función que determina la operación ingresada y llama la función correspondiente.
    """
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        transferencia()
    else:
        pass
