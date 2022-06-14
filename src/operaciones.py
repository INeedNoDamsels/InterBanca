"""
Operaciones disponibles del ATM.
"""
try:
    import menu
    import misc.interfaz
    from   misc.globales import tipo_cambio, lapso
except ImportError:
    import src.menu
    import src.misc.interfaz
    from misc.globales import tipo_cambio, lapso

def configuracion():
    """
    Función que habilita o deshabilita el paso del tiempo al ejecutar ciertas operaciones.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(0)

    opcion = input("¿Habilitar acciones con tiempo? (s/n): ")
    if opcion in ("s", "S"):
        misc.globales.tiempos = True
    elif opcion in ("n", "N"):
        misc.globales.tiempos = False
    else:
        configuracion()

def consulta():
    """
    Función que permite la consulta de saldo en la cuenta.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(1)

    opcion = int(input("\t\t     <1> Posición global <2> Movimientos\n\t\t\t\t  <3> Salir \
\n >> Ingrese operación: "))
    if opcion == 1:
        misc.globales.tipo_cambio()

        misc.interfaz.head()
        misc.interfaz.nombre_operacion(1)

        print(f"\t\t\tSaldo disponible: ${misc.globales.saldo} {misc.globales.moneda}")
        misc.interfaz.continuar()
    elif opcion == 2:
        pass # Movimientos
    else:
        menu.opciones()

    menu.opciones()

def retiro():
    """
    Función que permite el retiro de dinero.
    """
    misc.interfaz.head()

    misc.interfaz.nombre_operacion(1)

    tipo_cambio()
    retirar=int(input('Ingrese el monto a retirar'))
    try:
        assert 0<retirar<misc.globales.saldo
        cuenta=int(input('Ingrese la cuenta a debitar'))
        try:
            assert cuenta==misc.globales.cta_debitar
            valor=False
            cont2=0
            while valor==False: # while valor is False
                clave=int(input('Ingrese su clave nuevamente'))
                if clave==misc.globales.clave_a:
                    misc.globales.dinero -= retirar
                    preg2=int(input('Desea imprimir el voucher? <1> Si <2> No\n -->'))
                    if preg2==1:
                        print ('Imprimiendo')
                        lapso(2)
                        menu.opciones()
                    print('Realizado')
                    lapso(2)
                    menu.opciones()
                else:
                    if cont2<=1:
                        print ('Intente de nuevo:')
                        cont2+=1
                        valor=False
                    else:
                        print('Se agotaron los intentos')
                        lapso(1)
                        menu.opciones()
        except :
            misc.interfaz.head()
            misc.interfaz.nombre_operacion(1)
            print("\t\t\t     Cuenta inexistente")
    except:
        cont=1
        misc.interfaz.head()
        misc.interfaz.nombre_operacion(1)
        print("\t\t\t     Fondos insuficientes")
        print('Desea modificar el saldo? <1> Si <2> Salir\n Tiene solo un intento')
        preg=int(input('-->'))
        try:
            assert cont==misc.globales.intento
            if preg==1:
                misc.globales.intento+=1
                retiro()
            else:
                print ('Hasta pronto')
                lapso(1)
                menu.opciones()
        except:
            print('Se agotaron los intentos')
            lapso(1)
            misc.globales.intento-=1
            salir()

    lapso(2)
    menu.opciones()

def transferencia(intentos):
    """
    Función que permite la transferencia de dinero de una cuente a otra.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(3)

    clave = int(input(" >> Ingrese la clave de seguridad: "))
    if clave == misc.globales.clave_a:
        numero = int(input(" >> Ingrese número de cuenta destino: "))
        if numero == misc.globales.clave_b:
            tipo_cambio()

            monto = float(input("\n >> Ingrese monto: $"))
            if 0 < monto <= misc.globales.saldo:
                if misc.globales.moneda == "ARS":
                    misc.globales.dinero -= monto
                else:
                    misc.globales.dinero -= misc.globales.conversor_a_ars(monto)

                misc.interfaz.head()
                misc.interfaz.nombre_operacion(3)
                print("\t\t\t      Operación exitosa")

            else:
                misc.interfaz.head()
                misc.interfaz.nombre_operacion(3)
                print("\t\t\t     Saldo insuficiente")
        else:
            misc.interfaz.head()
            misc.interfaz.nombre_operacion(3)
            print("\t\t\t     Cuenta inexistente")
    else:
        intentos += 1

        if intentos == 3:
            misc.interfaz.final(1)
        else:
            transferencia(intentos)

    lapso(2)
    menu.opciones()

def salir():
    """
    Función que permite la salida voluntaria del usuario.
    """
    misc.interfaz.head()
    misc.interfaz.nombre_operacion(4)

    print("\t\t\t     Expulsando tarjeta")
    lapso(2)

    misc.interfaz.final(0)
