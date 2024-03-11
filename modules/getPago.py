import storage.pago as pa 

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
        
def menu():
    while True:
        print("""
Reportes de los pagos
0.Regresar a menu principal
1.Obtener el código de cliente de aquellos clientes que realizaron algún pago en 2008
2.Obtener todos los pagos que se realizaron en el año 2008 mediante Paypal
3.Obtener todas las formas de pago
""")
        opcion = int(input("\nSeleccione una de las opciones:"))
        if(opcion == 1):
            print(tabulate(getAllCodigosPagosAño(),tablefmt="grid"))
        elif(opcion == 2):
            print(tabulate(getAllAñoPaypal(),tablefmt="grid"))
        elif(opcion == 3):
            print(tabulate(getAllAñoFormasPa(),tablefmt="grid"))
        elif(opcion == 0):
            break
            