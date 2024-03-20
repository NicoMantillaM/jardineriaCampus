import os
import requests
from tabulate import tabulate

def getAllDataPagos():
    #json-server storage/pago.json -b 55011
    peticion=requests.get("http://154.38.171.54:5006/pagos")
    data= peticion.json()
    return data 

def getAllDataClient():
  #json-server storage/cliente.json -b 5507
  peticion=requests.get("http://154.38.171.54:5001/cliente")
  data= peticion.json()
  return data

def getAllDataEmpleado():
  #json-server storage/empleado.json -b 5508
  peticion=requests.get("http://154.38.171.54:5003/empleados")
  data= peticion.json()
  return data

def getAllIdTrans(id):
    for val in getAllDataPagos():
        if val.get("id_transaccion") == id:
            return [val]

def getAllFormasPago(formaPa):
    for val in getAllDataPagos():
        if (val.get("forma_pago")== formaPa):
            return val

#filtro 8
def getAllCodigosPagosAño():
    CodigosAño = []
    codigos_vistos = set()
    for val in getAllDataPagos():
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
    for val in getAllDataPagos():
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
    for val in getAllDataPagos():
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
    for val in getAllDataClient():
        for val2 in getAllDataPagos(): 
            for val3 in getAllDataEmpleado():
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
    for val in getAllDataClient():
        for val2 in getAllDataPagos(): 
            for val3 in getAllDataEmpleado():
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
        os.system ("clear")
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
                input("Presione una tecla para continuar..........")
            elif(opcion == 2):
                    print(tabulate(getAllAñoPaypal(),tablefmt="grid"))
                    input("Presione una tecla para continuar..........")
            elif(opcion == 3):
                    print(tabulate(getAllAñoFormasPa(),tablefmt="grid"))
                    input("Presione una tecla para continuar..........")
            elif(opcion == 4):
                    print(tabulate(getAllClientsPagos(),tablefmt="grid"))
                    input("Presione una tecla para continuar..........")
            elif(opcion == 5):
                    print(tabulate(getAllClientsNoPagos(),tablefmt="grid"))
                    input("Presione una tecla para continuar..........")
            elif(opcion == 0):
                    break
        except KeyboardInterrupt:
            break
             
             
            