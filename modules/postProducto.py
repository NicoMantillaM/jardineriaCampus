import os
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG

def postProducto():
    #json-server storage/producto.json -b 5505
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    }


    peticion = requests.post("http://172.16.100.115:5505", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print ("""
ADMINISTRAR DATOS DE PRODUCTOS
0.Regresar al menu principal
1.Guardar un producto nuevo
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postProducto(), tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break

