"""
Funciones útiles y variables globales.
"""

import time

saldo_ar = 85000 # única variable que puede cambiar durante la ejecución del programa.
clave_a  = 12345
clave_b  = 98765
dni      = 12345678
sol      = 0.0419294118

def lapso(segundos):
    """
    Función que simula la realización de algunas tareas internas del ATM, para agregar "realismo".
    """
    for i in range(segundos):
        time.sleep(1)

def tipo_cambio():
    """
    Función que determina el monto y moneda de referencia que utilizará el programa.
    """
    global moneda
    global saldo

    opcion = (int(input("\n >> Ingrese tipo de moneda (<1> ARS, <2> PER): ")))
    try:
        assert 1 <= opcion <= 2
        if opcion == 1:
            moneda = "ARS"
        else:
            moneda = "PER"
    except:
        tipo_cambio()

def conversor(saldo):
    """
    Función que convierte el saldo a la moneda de referencia.
    """

    if moneda == "PER":   # ARS a PER
        dinero = round(saldo * sol, 2)
    elif moneda == "ARS": # PER a ARS
        dinero = saldo / sol

    return dinero
