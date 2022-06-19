################
# Agustina Bover    @Agustina-Bover
# Manuel   Bernabei @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test correspondientes al archivo 'operaciones'.
"""
#!/usr/bin/python

from src.operaciones import retiro
from src.misc.globales import tipo_cambio

#Testing: Retiro
def test_retiro_clave_correcta_imprimir_ticket():
    contra=12345
    cantidad=5000
    preg=1

    moneda = "ARS"

    resultado=retiro(contra,cantidad,preg, moneda)
    assert isinstance(resultado,int), "El resultado debe ser un nro"
    assert resultado==2,"No se obtiene el resultado esperado"

def test_retiro_clave_correcta_no_imprimir_ticket():
    contra=12345
    cantidad=5000
    preg=2
    moneda="ARS"
    resultado=retiro(contra,cantidad,preg)
    assert isinstance(resultado,int), "El resultado debe ser un nro"
    assert resultado==1,"No se obtiene el resultado esperado"

def test_retiro_clave_incorrecta():
    clave=123
    monto=5000
    pregunta=1
    resultado=retiro(clave,monto,pregunta)
    assert isinstance(resultado,int), "El resultado debe ser un nro"
    assert resultado==0,"No se obtiene el resultado esperado"
