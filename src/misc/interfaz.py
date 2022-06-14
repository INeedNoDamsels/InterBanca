"""
Interfaces y demás extras para simular realismo.
"""
from os import system, name
try:
    from menu          import inicio
    from operaciones   import configuracion
    from misc.globales import lapso
except ImportError:
    from src.menu          import inicio
    from src.operaciones   import configuracion
    from src.misc.globales import lapso

def nombre_operacion(posicion):
    """
    Función que imprime el nombre correspondiente a cada operación.
    """
    nombres = ("[CONFIGURACIÓN]", "[  CONSULTAS  ]", "[   RETIROS   ]",
               "[TRANSFERENCIA]", "[FINALIZANDO]")

    print(f"\n\t\t\t       {nombres[posicion]}\n")

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
    lapso(2)

    head()
    print("\n\t\t\t     Leyendo tarjeta")
    lapso(2)

    inicio(0)

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
    mensajes = ("\n\t\t\t      Guarde su tarjeta \
\n\t\t     Gracias por confiar en InterBanca ©",
                "\n\t       Demasiados intentos fallidos, tarjeta retenida \
\n\t  Para más información, contacte a su proveedor de tarjetas")

    head()
    print(mensajes[nro_mensaje])
    lapso(3)
    activacion()
