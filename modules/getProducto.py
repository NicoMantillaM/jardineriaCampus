import os
from tabulate import tabulate
import requests

def getAllData():
    #json-server storage/producto.json -b 5505
    peticion=requests.get("http://172.16.103.38:5505")
    data= peticion.json()
    return data
    
#Devuelve un listado con todas los productos q pertenecen a la gama ornamentales
#y q tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta, mayor a menor

def getAllStocksPriceGama():
    stockPriceGama = []
    for val in getAllData():
        gama = val.get('gama')
        stock = val.get('cantidad_en_stock')
        if gama == 'Ornamentales' and stock >= 100:
            stockPriceGama.append({
                'codigo_producto': val.get('codigo_producto'),
                'nombre': val.get('nombre'),
                'gama': val.get('gama'),
                'cantidad_en_stock': val.get('cantidad_en_stock'),
                'precio_venta': val.get('precio_venta')
            })
    stockPriceGama.sort(key=lambda x: x['precio_venta'], reverse=True)
    return stockPriceGama

def menu():
    while True:
        os.system ("clear")
        print("""
REPORTES DE LOS PRODUCTOS
0.Regresar al menu principal
1.Obtener todos los productos de una categoria ordenando su precio de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100 )

    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        try:
            opcion=int(input("Seleccione una de las opciones: "))
            if (opcion==1):
                print(tabulate(getAllStocksPriceGama(),tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break

