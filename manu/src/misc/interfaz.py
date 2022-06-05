"""
Encabezado del software.
"""

import os
from menu import inicio
from .globales import lapso

def head():
    """
    Función que imprime ese interfaz tan querido por la comunidad bancaria Peruana-Argentina.
    """
    os.system('cls')

    print("\n _  _    _  _______  ______  _____    _____    ____   _    _    ____   ____ \
    \n| || \\  | ||__   __||  ____||  __ \\  |  __ \\  / __ \\ | \\  | |  / ___| / __ \\ \
    \n| ||  \\ | |   | |   | |     | |  \\ \\ | |  \\ \\| /  \\ ||  \\ | | / /    | /  \\ | \
    \n| ||   \\| |   | |   | |___  | |__/ / | |__/ /| |__| ||   \\| || |     | |__| | \
    \n| ||      |   | |   |  ___| |  _  /  |  __ | |  __  ||      || |     |  __  | \
    \n| || |\\   |   | |   | |     | | \\ \\  | |  \\ \\| |  | || |\\   || |     | |  | | \
    \n| || | \\  |   | |   | |____ | |  \\ \\ | |__/ /| |  | || | \\  | \\ \\___ | |  | | \
    \n|_||_|  \\_|   |_|   |______||_|   \\_\\|_____/ |_|  |_||_|  \\_|  \\____||_|  |_|")

def activacion():
    """
    Función que simula la inicialización del ATM, el ingreso y lectura de la tarjeta.
    """
    head()
    input("\n\t\t\tPresione Enter para continuar ")

    head()
    print("\n\t\t       Ingrese la tarjeta en la ranura")
    lapso(3)

    head()
    print("\n\t\t\t     Leyendo tarjeta")
    lapso(3)

    inicio(0)

def final(mensaje):
    """
    Función que finaliza la ejecución del programa, producida lo que especifica en el mensaje.
    """
    head()
    print(mensaje)
    lapso(5)