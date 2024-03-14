import os
from tabulate import tabulate
import requests

def getAllData():
    #json-server storage/producto.json -b 5505
    peticion=requests.get("http://172.16.100.115:5505")
    data= peticion.json()
    return data
    
#Devuelve un listado con todas los productos q pertenecen a la gama ornamentales
#y q tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta, mayor a menor

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):    
        condiciones[i] = {
        "codigo": val.get("codigo_producto"), 
        "venta": val.get("precio_venta"),
        "nombre": val.get("nombre_producto"),   
        "gama": val.get("gama"), 
        "dimensiones": val.get("dimensiones"),
        "proveedor": val.get("proveedor"),              
        "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
        "stock": val.get("cantidad_stock"),
        "base": val.get("precio_proveedor")
        }
    return condiciones

def menu():
    while True:
        os.system("clear")
        print("""
REPORTES DE LOS PRODUCTOS
0.Regresar al menu principal
1.Obtener todos los productos de una categoria ordenando su precio de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100 )

    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        try:
            opcion=int(input("Seleccione una de las opciones: "))
            if (opcion==1):
                gama=input("Ingrese la gama que desea del producto: ")
                stock=int(input("Ingrese las unidades que desea mostrar: "))
                print(tabulate(getAllStocksPriceGama(gama,stock),tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break
