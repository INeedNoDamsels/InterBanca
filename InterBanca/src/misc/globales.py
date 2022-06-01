"""
Funciones útiles y variables globales.
"""

#####
# IMPORTANTE:
# tener en cuenta que las variables deben ser de tipo float, ya que son números positivos decimales.
#####

saldoAR = 85000 # Única variable que puede cambiar durante la ejecución del programa.
clave   = 12345
dni     = 12345678
sol     = 0.0419294118
nro_cuenta_dos = 98765

def conversorPE(saldoAR):
    """
    Conversor de pesos argentinos (AR) a soles peruanos (PE).
    """
    return round(saldoAR * sol, 2)

def tipo_cambio(moneda):
    """
    Función que determina el monto y moneda de referencia que utilizará el programa.
    """
    monto = 0
    tipo  = ""

    if moneda == 1:
        monto = saldoAR
        tipo  = "AR$"
    else:
        monto = conversorPE(saldoAR)
        tipo  = "PER"
    return monto, tipo
