"""
Inicialización del ATM y menú de opciones.
"""
try:
    import main
    import operaciones
    import misc.globales
except ImportError:
    import src.main
    import src.operaciones
    import src.misc.globales

def validar_datos(dato, almacenado):
    """
    Función que valida el dato recibido con su contraparte almacenada.
    """
    dato_validado = bool(dato == almacenado)

    return dato_validado

def inicio(clave, documento):
    """
    Función que verifica la clave de seguridad y documento del usuario.
    """
    usuario_validado = bool((validar_datos(clave, 12345) is True) and (validar_datos(documento, 12345678) is True))

    return usuario_validado

def operacion(opcion):
    """
    Función que redirige al usuario a la operacion deseada.
    """
    codigo = 0

    if opcion != 4:
        tipo_moneda = main.ingreso_valor(1, 2, 0, ">> Ingrese tipo de moneda (<1> ARS <2> PER): ")
        moneda, saldo = misc.globales.tipo_cambio(tipo_moneda)

    if opcion == 1:
        opcion_b = main.ingreso_valor(1, 2, 3, "<1> Posicion global <2> Movimientos: ")
        operaciones.consulta(opcion_b, moneda, saldo)
    elif opcion == 2:
        clave    = main.ingreso_valor(10000, 99999, 4, ">> Ingrese su clave: " )
        monto    = main.ingreso_valor(0, saldo, 4, ">> Ingrese el monto a retirar (<0> Salir): $")
        pregunta = main.ingreso_valor(1, 2, 4, "¿Desea imprimir el voucher? (<1> Si <2> No): ")

        codigo   = operaciones.retiro(clave, monto, pregunta, moneda)
    elif opcion == 3:
        clave  = main.ingreso_valor(10000, 99999, 5, ">> Ingrese el número de cuenta destino: ")
        monto  = main.ingreso_valor(0, saldo, 5, ">> Ingrese el monto a transferir (<0> Salir): $")

        codigo = operaciones.transferencia(clave, monto, moneda)
    else:
        operaciones.salir()

    return codigo
