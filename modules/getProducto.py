
from tabulate import tabulate
import json
import requests
def getAllData():
    #json-server storage/producto.json -b 5501
    peticion=requests.get("http://172.16.100.110:5503")
    data= peticion.json()
    return data
    

#Devuelve un listado con todas los productos q pertenecen a la gama ornamentales
#y q tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta, mayor a menor

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData:
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
        print("""
REPORTES DE LOS PRODUCTOS
0.Regresar al menu principal
1.Obtener productos de una categoria ordenando su precio de venta y rectificando que su cantidad de stock sea superior
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        try:
            opcion=int(input("Seleccione una de las opciones: "))
            if (opcion==1):
                gama=input("Ingrese la gama del producto: ")
                stock=int(input("Ingrese el stock del producto: "))
                print(tabulate(getAllStocksPriceGama(gama,stock),headers="keys",tablefmt="grid"))
            elif(opcion==2):
                producto= { 
                "codigo_producto": input("Ingrese el codigo producto"),
                    "nombre": input("Ingrese el nombre del producto"),
                    "gama": input("Ingrese el gama del producto"),
                    "dimensiones": input("Ingrese las dimensiones del producto"),
                    "proveedor": input("Ingrese el proveedor del producto"),
                    "descripcion":input ("ingrese descripcion del producto"),
                    "cantidad_en_stock": int("15"),
                    "precio_venta": int("14"),
                    "precio_proveedor":int ("11")
            }
        except KeyboardInterrupt:
            break
