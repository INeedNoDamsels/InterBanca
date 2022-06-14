################
# Agustina Bover    @Agustina-Bover
# Manuel   Bernabei @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Programa ppal.
"""
try:
    from misc.interfaz import activacion
except ImportError:
    from src.misc.interfaz import activacion

def principal():
    """
    Función que permite el inicio de tus aventuras con la ATM.
    """
    activacion()

if __name__ == "__main__":
    principal()
