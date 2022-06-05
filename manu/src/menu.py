"""
Inicialización del ATM y menú de opciones.
"""
import misc.interfaz
import misc.globales
from operaciones import *

def inicio(intentos):
    """
    Función que solicita el ingreso de la clave de seguridad.
    """
    misc.interfaz.head()

    clave = int(input("\n>> Ingrese la clave de seguridad : "))
    docu  = int(input(">> Ingrese su número de documento: "))
    try:
        assert (clave == misc.globales.clave_a) and (docu == misc.globales.dni)
        opciones()
    except:
        intentos += 1

        if intentos == 3:
            misc.interfaz.final("\n\t       Demasiados intentos fallidos, tarjeta retenida \
\n\t  Para más información, contacte a su proveedor de tarjetas")
        else:
            inicio(intentos)

def opciones(): # Aca no hace falta agregar nada ;)
    """
    Función que imprime las opciones disponibles.
    """
    misc.interfaz.head()

    opcion = int(input("\n\t\t\t\t Bienvenido \
\n\n\t\t <1> Consultas <2> Retiros <3> Transferencia\n\t\t\t\t  <4> Salir \
\n >> Ingrese operación: "))

    try:
        assert 0 < opcion < 5
        operacion(opcion)
    except:
        opciones()

def operacion(opcion): # Agregar condicional y llamar función correspondiente.
    """
    Función que determina la operación ingresada y llama la función correspondiente.
    """
    misc.interfaz.head()

    if opcion == 1:
        consulta()
    elif opcion == 2:
        retiro()
    elif opcion == 3:
        transferencia()
    else:
        salir()
