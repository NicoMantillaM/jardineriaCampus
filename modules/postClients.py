import os
from tabulate import tabulate
import json
import requests

def postClients():
    #json-server storage/cliente.json -b 5507
    cliente = { 
        "codigo_cliente": int(input("Ingrese el codigo del cliente : ")),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido del contacto: "),
        "telefono": input("Ingrese el telefono del cliente : "),
        "fax": input("Ingrese el fax  del cliente : "),
        "linea_direccion1": input("Ingrese la direccion #1 del cliente : "),
        "linea_direccion2":input("Ingrese la direccion #2 del cliente : "),
        "ciudad": input("Ingrese la ciudad del cliente : "),
        "region": input("Ingrese la region del cliente : "),
        "pais": input("Ingrese el pais del cliente : "),
        "codigo_postal": input("Ingrese el codigo postal del cliente : "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del representante de ventas : ")),
        "limite_credito": int(input("Ingrese el limite del credito: "))
    }

    peticion = requests.post("http://192.168.1.11:5507", data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE CLIENTES
0.Regresar al menu principal
1.Guardar un cliente nuevo
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postClients(), tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break
