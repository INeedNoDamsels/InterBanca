################
# Agustina Bover    @Agustina-Bover
# Manuel   Bernabei @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test correspondientes al archivo 'operaciones'.
"""
#!/usr/bin/python

from src.operaciones import retiro, transferencia
from src.misc.globales import tipo_cambio

#Testing: Retiro
def test_retiro_clave_correcta_imprimir_ticket():
    """
    Comprueba el buen funcionamiento en caso de que el retiro
    sea exitoso y se quiera imprimir el ticket
    """
    contra=12345
    cantidad=5000
    preg=1

    moneda = "ARS"

    resultado=retiro(contra,cantidad,preg, moneda)
    assert isinstance(resultado,int), "El resultado debe ser un nro"
    assert resultado==2,"No se obtiene el resultado esperado"

def test_retiro_clave_correcta_no_imprimir_ticket():
    """
    Comprueba el buen funcionamiento en caso de que el retiro
    sea exitoso y no se quiera imprimir el ticket
    """
    contra=12345
    cantidad=5000
    preg=2
    moneda="ARS"
    resultado=retiro(contra,cantidad,preg, moneda)
    assert isinstance(resultado,int), "El resultado debe ser un nro"
    assert resultado==1,"No se obtiene el resultado esperado"

def test_retiro_clave_incorrecta():
    """
    Comprueba el buen funcionamiento en caso de que la contraseña
    sea incorrecta
    """
    clave=123
    monto=5000
    pregunta=1
    moneda="ARS"
    resultado=retiro(clave,monto,pregunta, moneda)
    assert isinstance(resultado,int), "El resultado debe ser un nro"
    assert resultado==0,"No se obtiene el resultado esperado"
#testing: trasferencia
def  test_transferencia_clave_incorrecta():
    """
    Comprueba el buen funcionamiento en caso de que
    la cuenta bancaria destino sea incorrecta
    """
    clave=123
    monto=15000
    moneda= "ARS"
    resultado=transferencia(monto,clave,moneda)
    assert isinstance (resultado, int), "el resultado debe ser un nro"
    assert resultado==0,"No se obtiene el resultado esperado"
def  test_transferencia_clave_correcta_exitosa():
    """
    Comprueba el buen funcionamiento en caso de que la transferencia
    sea exitosa
    """
    clave=98765
    monto=5000
    moneda="ARS"
    resultado=transferencia(clave,monto,moneda)
    assert isinstance (resultado,int), "El resultado debe ser un nro"
    assert resultado==1, "no se obtiene el resultado esperado"