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
def test_conversor_a_per():
    valor=5000
    resultado=conversor_a_per(valor)
    assert isinstance (resultado, float), "el resultado debe ser un nro"
    assert resultado==209.65, "No se obtiene el resultado esperado"
def test_conversor_a_ars():
    valor=300
    resultado=conversor_a_ars(valor)
    assert isinstance (resultado, float), "el resultado debe ser un nro"
    assert resultado==7154.88, "No se obtiene el resultado esperado"
