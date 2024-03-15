#import storage.pago as pa 
#import storage.cliente as cli
#import storage.empleado as em 
from tabulate import tabulate

#filtro 8
def getAllCodigosPagosAño():
    CodigosAño = []
    codigos_vistos = set()
    for val in pa.pago:
        if "2008" in val.get("fecha_pago"):
            codigo_cliente = val.get("codigo_cliente")
            if codigo_cliente not in codigos_vistos:
                CodigosAño.append(
                    {
                        "codigo_cliente": codigo_cliente,
                        "fecha": val.get("fecha_pago"),
                        "total": val.get("total")
                    }
                )
                codigos_vistos.add(codigo_cliente)
    return CodigosAño

#pagos- filtro 13
def getAllAñoPaypal():
    pagosPaypal= []
    for val in pa.pago:
        if ("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"): 
            pagosPaypal.append({
                "codigo_cliente": val.get ("codigo_cliente"),
                "forma_pago": val.get ("forma_pago"),
                "fecha_pago": val.get ("fecha_pago"),
                "total": val.get ("total")
             })
    pagosPaypal= sorted(pagosPaypal, key=lambda x: x  ["total"], reverse=True )
    return pagosPaypal

#formas pagos_ filtro 14
def getAllAñoFormasPa():
    formaspago= []
    formasVistas= set()
    for val in pa.pago:
        forma_pago= ("forma_pago")
        if forma_pago not in ("formasVistas"):
            formaspago.append({ 
                "codigo_cliente":val.get("codigo_cliente"),
                "forma_pago":val.get("forma_pago"),
                "total":val.get("total")
            })
    formasVistas.add(forma_pago)

    return formaspago 

def getAllClientsPagos():
    clientespago= []
    for val in cli.clientes:
        for val2 in pa.pago: 
            for val3 in em.empleado:
                if val2.get("codigo_cliente")== val.get("codigo_cliente") and val.get("codigo_empleado_rep_ventas")== val3.get("codigo_empleado"):
                        clientespago.append(
                            {
                            "codigo_cliente": val.get("codigo_cliente"),
                            "nombre_cliente": val.get("nombre_cliente"),
                            "nombre": val3.get("nombre")
                            }
                            )
    return clientespago

def getAllClientsNoPagos():
    clientesNopago= []
    for val in cli.clientes:
        for val2 in pa.pago: 
            for val3 in em.empleado:
                if not val2.get("codigo_cliente")== val.get("codigo_cliente") and val.get("codigo_empleado_rep_ventas")== val3.get("codigo_empleado"):
                        clientesNopago.append(
                            {
                            "codigo_cliente": val.get("codigo_cliente"),
                            "nombre_cliente": val.get("nombre_cliente"),
                            "nombre": val3.get("nombre")
                            }
                            )
    return clientesNopago
     

def menu():
    while True:
        print("""
Reportes de los pagos
0.Regresar a menu principal
1.Obtener el código de cliente de aquellos clientes que realizaron algún pago en 2008
2.Obtener todos los pagos que se realizaron en el año 2008 mediante Paypal
3.Obtener todas las formas de pago
4.Obtener todos los clientes que hayan realizado pagos, junto con sus representantes de ventas
5.Obtener todos los clientes que no realizaron pagos, junto con sus representantes de ventas
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        try:
            opcion = int(input("\nSeleccione una de las opciones:"))
            if(opcion == 1):
                print(tabulate(getAllCodigosPagosAño(),tablefmt="grid"))
            elif(opcion == 2):
                    print(tabulate(getAllAñoPaypal(),tablefmt="grid"))
            elif(opcion == 3):
                    print(tabulate(getAllAñoFormasPa(),tablefmt="grid"))
            elif(opcion == 4):
                    print(tabulate(getAllClientsPagos(),tablefmt="grid"))
            elif(opcion == 5):
                    print(tabulate(getAllClientsNoPagos(),tablefmt="grid"))
            elif(opcion == 0):
                    break
        except KeyboardInterrupt:
            break
             
             
            