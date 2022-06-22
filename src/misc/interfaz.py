"""
Interfaces y demás extras para simular realismo.
"""
import sys
from os import system, name
try:
    from misc.globales import lapso
    from operaciones   import configuracion
except ImportError:
    from src.misc.globales import lapso
    from src.operaciones   import configuracion

def nombre_operacion(posicion):
    """
    Función que imprime el nombre correspondiente a cada operación.
    """
    nombres = ("", "[  ACCEDIENDO ]\n", "[CONFIGURACIÓN]\n", "[  CONSULTAS  ]\n",
                   "[   RETIROS   ]\n", "[TRANSFERENCIA]\n", "[ ABANDONANDO ]\n")

    print(f"\n\t\t\t       {nombres[posicion]}")

def head():
    """
     Función que limpia la pantalla
    e imprime ese interfaz tan querido por la comunidad bancaria Peruana-Argentina.
    """
    if name == "nt":      # para Windows
        _ = system("cls")
    elif name == "posix": # para Mac / Linux
        _ = system("clear")

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
    lapso()

    head()
    print("\n\t\t\t     Leyendo tarjeta")
    lapso()

def continuar():
    """
    Función que solicita al usuario interacción con el ATM para continuar su ejecución.
    """
    _ = input("\n\t\t\tPresione Enter para continuar ")
    if _ == "0":
        configuracion()

def final(nro_mensaje):
    """
    Función que cierra la sesión actual, producida lo que especifica en el mensaje.
    """
    mensajes = ("\t\t\t      Guarde su tarjeta \n\t\t     Gracias por confiar en InterBanca ©",
"\t       Demasiados intentos fallidos, tarjeta retenida\
\n\t  Para más información, contacte a su proveedor de tarjetas")

    head()
    nombre_operacion(6)
    print(f"{mensajes[nro_mensaje]}")
    sys.exit()
