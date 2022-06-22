"""
Funciones útiles.
"""
from time import sleep

# pylint: disable=C0103

tiempos = True  #
dinero  = 85000 # única variable que puede cambiar durante la ejecución del programa.
sol     = 0.0419294118

# pylint: enable-msg=C0103

def lapso():
    """
    Función que simula la realización de algunas tareas internas del ATM, para agregar "realismo".
    """
    segundos = 2

    if tiempos is False:
        segundos = 0

    for _ in range(segundos):
        sleep(1)

def tipo_cambio(opcion):
    """
    Función que determina el monto y moneda de referencia que utilizará el programa.
    """

    if opcion == 1:
        moneda = "ARS"
        saldo  = round(dinero, 2)
    else:
        moneda = "PER"
        saldo  = conversor_a_per(dinero)

    return moneda, saldo

def conversor_a_per(valor):
    """
    Función que convierte de ARS a PER.
    """
    return round(valor * sol, 2)

def conversor_a_ars(valor):
    """
    Función que convierte de PER a ARS.
    """
    return round(valor / sol, 2)
