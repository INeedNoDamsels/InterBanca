"""
Funciones útiles y variables globales.
"""
from time import sleep

dinero  = 85000 # única variable que puede cambiar durante la ejecución del programa.
clave_a = 12345
clave_b = 98765
dni     = 12345678
sol     = 0.0419294118

def lapso(segundos):
    """
    Función que simula la realización de algunas tareas internas del ATM, para agregar "realismo".
    """
    for i in range(segundos): # ¡ Cambiar 'segundos' por '0' para mayor rapidez !
        sleep(1)

def tipo_cambio():
    """
    Función que determina el monto y moneda de referencia que utilizará el programa.
    """
    global moneda
    global saldo

    opcion = (int(input(" >> Ingrese tipo de moneda (<1> ARS, <2> PER): ")))
    if opcion == 1:
        moneda = "ARS"
        saldo  = round(dinero, 2)
    elif opcion == 2:
        moneda = "PER"
        saldo  = conversor_a_per(dinero)
    else:
        tipo_cambio()

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
