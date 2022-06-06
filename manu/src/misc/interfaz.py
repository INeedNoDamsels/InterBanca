"""
Interfaces y demás extras para simular realismo.
"""
import os
from .globales import lapso
from menu      import inicio

def nombre_operacion(posicion):
    nombres = ("[  CONSULTAS  ]", "[   RETIROS   ]", "[TRANSFERENCIA]", "[FINALIZANDO]")
    print(f"\n\t\t\t\t{nombres[posicion]}\n")

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
    continuar()

    head()
    print("\n\t\t       Ingrese la tarjeta en la ranura")
    lapso(3)

    head()
    print("\n\t\t\t     Leyendo tarjeta")
    lapso(3)

    inicio(0)

def continuar():
    """
    Función que solicita al usuario interacción con el ATM para continuar su ejecución.
    """
    input("\n\t\t\tPresione Enter para continuar ")

def final(mensaje):
    """
    Función que cierra la sesión actual, producida lo que especifica en el mensaje.
    """
    head()
    print(mensaje)
    lapso(5)
    activacion()
