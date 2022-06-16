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
    usuario_validado = bool((clave == misc.globales.clave_a) and (documento == misc.globales.dni))

    return usuario_validado

def operacion(opcion):
    """
    Función que redirige al usuario a la operacion deseada.
    """
    if opcion != 4:
        tipo_moneda = main.ingreso_valor(1, 2, 0, ">> Ingrese tipo de moneda (<1> ARS <2> PER): ")
        misc.globales.tipo_cambio(tipo_moneda)

    if opcion == 1:
        operacion = main.ingreso_valor(1,2,3, "<1> Posicion global <2> Movimientos: ")
        operaciones.consulta(operacion)
    elif opcion == 2:
        clave    = main.ingreso_valor(0, 99999, 4, ">> Ingrese su clave: " )
        monto    = main.ingreso_valor(0, misc.globales.saldo , 4, ">> Ingrese el monto a retirar (<0> Salir): $")
        pregunta = main.ingreso_valor(1,2,4,"¿Desea imprimir el voucher? (<1> Si <2> No): ")

        codigo   = operaciones.retiro(clave,monto,pregunta)
    elif opcion == 3:
        clave  = main.ingreso_valor(0, 99999, 5, ">> Ingrese el número de cuenta destino: ")
        monto  = main.ingreso_valor(100, 85000, 5, ">> Ingrese el monto para transferir (<0> Salir): $")

        codigo = operaciones.transferencia(clave, monto)
    else:
        operaciones.salir()

    if 2 <= opcion <= 3:
        if codigo == 0:
            print("\t\t\t      Operación exitosa")
        elif codigo == 2:
            print("\t\t\t      Operación exitosa\n\t\t\t\t Imprimiendo")
        else:
            print("\t\t\t      Operación fallida")

        misc.globales.lapso()

    main.opciones()
