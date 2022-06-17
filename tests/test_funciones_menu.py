################
# Agustina Bover    @Agustina-Bover
# Manuel   Bernabei @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test correspondientes al archivo 'menu'.
"""
#!/usr/bin/python

from src.menu import validar_datos, inicio

# testing: validar_datos(dato, almacenado)
def test_validar_datos_correcto():
    """
    Test que evalúa la validación de dos datos, ambos correctos.
    """
    dato       = 98765
    almacenado = 98765 # misc.globales.clave_b
    resultado = validar_datos(dato, almacenado)
    assert resultado is True, "El resultado no es el esperado."

def test_validar_datos_incorrecto():
    """
    Test que evalúa la validación de dos datos, ambos incorrectos.
    """
    dato       = 12345
    almacenado = 98765 # misc.globales.clave_b
    resultado = validar_datos(dato, almacenado)
    assert resultado is False, "El resultado no es el esperado."

# testing: inicio(clave, documento)
def test_inicio_ambos_correctos():
    """
    Test que evalúa la validación inicial al ingresar ambos datos correctamente.
    """
    clave     = 12345    # misc.globales.clave_a
    documento = 12345678 # misc.globales.dni
    resultado = inicio(clave, documento)
    assert resultado is True, "El resultado no es el esperado."

def test_inicio_primero_correcto():
    """
    Test que evalúa la validación inicial al ingresar correctamente solo el 1er dato.
    """
    clave     = 12345    # misc.globales.clave_a
    documento = 87654321
    resultado = inicio(clave, documento)
    assert resultado is False, "El resultado no es el esperado."

def test_inicio_segundo_correcto():
    """
    Test que evalúa la validación inicial al ingresar correctamente solo el 2do dato.
    """
    clave     = 54321
    documento = 12345678 # misc.globales.dni
    resultado = inicio(clave, documento)
    assert resultado is False, "El resultado no es el esperado."

def test_inicio_ambos_incorrectos():
    """
    Test que evalúa la validación inicial al ingresar ambos datos incorrectamente.
    """
    clave     = 54321
    documento = 87654321
    resultado = inicio(clave, documento)
    assert resultado is False, "El resultado no es el esperado."
