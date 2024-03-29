import os
from tabulate import tabulate
import requests
import modules.getGamas as gG

def getAllData():
    #json-server storage/producto.json -b 5505
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data

#PARA VALIDAR POR MEDIO DE(CODIGO) SI EL PRODUCTO EXISTE
def getProductoCodigo(codigo):
   peticion = requests.get(f"http://154.38.171.54:5008/productos/{codigo}") 
   return [peticion.json()] if peticion.ok else[]

def getProductoCodigo2(codigo):
    for val in getAllData():
        if (val.get("codigo_producto")== codigo):
            return [{val}]
        


#Devuelve un listado con todas los productos q pertenecen a la gama ornamentales
#y q tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta, mayor a menor

def getAllStocksPriceGama():
    stockPriceGama = []
    for val in getAllData():
        gama = val.get('gama')
        stock = val.get('cantidadEnStock')
        if gama == 'Ornamentales' and stock >= 100:
            stockPriceGama.append({
                'codigo_producto': val.get('codigo_producto'),
                'nombre': val.get('nombre'),
                'gama': val.get('gama'),
                'cantidadEnStock': val.get('cantidadEnStock'),
                'precio_venta': val.get('precio_venta')
            })
        else:
            print("noxd")
    stockPriceGama.sort(key=lambda x: x['precio_venta'], reverse=True)
    return stockPriceGama



def getAllProductosOrnamentales(gama,stock):
    condiciones=[]
    for val in getAllData():
        if(val.get("gama")==gama) and (val.get("cantidadEnStock")>=stock):
            condiciones.append(val)
        def price(val):
            return val.get("precio_venta")
        condiciones.sort(key=price, reverse=True)
        for i, val in enumerate(condiciones):
            condiciones[i]={
            "Codigo del Producto":val.get("codigo_producto"),
            "Nombre":val.get("nombre"),
            "Gama":val.get("gama"),
            "Cantidad en stock":val.get("cantidadEnStock"),
            "Precio de venta":val.get("precio_venta"),
            "Precio al proveedor":val.get("precio_proveedor")
        }

    return condiciones

def menu():
    while True:
        os.system ("clear")
        print("""
REPORTES DE LOS PRODUCTOS
0.Regresar al menu principal
1.Obtener todos los productos de la categoria Ornamentales, ordenando su precio de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100 )
2.Obtener todos los productos de una categoria  ordenando su precio de venta, también que su cantidad de inventario sea superior            

    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        try:
            opcion=int(input("Seleccione una de las opciones: "))
            if (opcion==1):
                print(tabulate(getAllStocksPriceGama(),tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            if (opcion==2):   
                gama= gG.getAllNombre()[(int(input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))))]
                stock=int(input("Ingrese el stock del producto: "))
                print(tabulate(getAllProductosOrnamentales(gama,stock),tablefmt="grid"))
                input("Presiona cualquier tecla para continuar.....")
        
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break

