################
# Agustina Bover    @Agustina-Bover
# Manuel   Bernabei @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test correspondientes al archivo 'globales'.
"""
#!/usr/bin/python

from src.misc.globales import tipo_cambio, conversor_a_per, conversor_a_ars

#testing: conversor_a_per(valor)
def test_tipo_cambio_1():
    """
    Test que evalúa el correcto funcionamiento de la función tipo cambio en caso de seleccionar la opcion 1.
    """
    opcion = 1
    resultados = tipo_cambio(opcion)
    assert resultados == ("ARS", 85000), "El resultado no es el esperado."

def test_tipo_cambio_2():
    """
    Test que evalúa el correcto funcionamiento de la función tipo cambio en caso de seleccionar la opcion 2.
    """
    opcion = 2
    resultados = tipo_cambio(opcion)
    assert resultados == ("PER", 3564.0), "El resultado no es el esperado."

def test_conversor_a_per():
    """
    Comprueba el buen funcionamiento en caso de que se deba
    realizar una conversion a soles
    """
    valor=5000
    resultado=conversor_a_per(valor)
    assert isinstance (resultado, float), "el resultado debe ser un nro"
    assert resultado==209.65, "No se obtiene el resultado esperado"
def test_conversor_a_ars():
    """
    Comprueba el buen funcionamiento en caso de que se deba
    realizar una conversion a pesos
    """
    valor=300
    resultado=conversor_a_ars(valor)
    assert isinstance (resultado, float), "el resultado debe ser un nro"
    assert resultado==7154.88, "No se obtiene el resultado esperado"
