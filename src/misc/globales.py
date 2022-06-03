"""
Funciones útiles y variables globales.
"""

import time

saldo_ar = 85000
clave_A  = 12345
clave_B  = 98765
dni      = 12345678
sol      = 0.0419294118

def lapso():
    """
    Función que simula la realización de algunas tareas internas del ATM, para agregar "realismo".
    """
    for i in range(3):
        time.sleep(1)

def conversor():
    """
    Función que convierte pesos argentinos (AR) a soles peruanos (PE).
    """
    return round(saldo_ar * sol, 2)

def tipo_cambio():
    """
    Función que determina el monto y moneda de referencia que utilizará el programa.
    """
    opcion = (int(input("\n >> Ingrese tipo de moneda (<1> ARS, <2> PER): ")))

    if opcion == 1:
        saldo  = saldo_ar
        moneda = "ARS"
    else:
        saldo  = conversor()
        moneda = "PER"
