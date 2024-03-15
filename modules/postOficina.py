import os
from tabulate import tabulate
import json
import requests

def postOficina():
    #json-server storage/oficina.json -b 5509
    oficina = {
        
        "codigo_oficina": int(input("Ingrese el codigo del oficina : ")),
        "ciudad": input("Ingrese la ciudad de la oficina: "),
        "pais": input("Ingrese el pais de la oficina: "),
        "region": input("Ingrese la region de la oficina: "),
        "codigo_postal": input("Ingrese el codigo postal: ") ,
        "telefono": input("Ingrese el telefono de la oficina: "),
        "linea_direccion1": input("Ingrese la direccion #1 de la oficina: "),
        "linea_direccion2": input("Ingrese la direccion #2 de la oficina: ")
    }

    peticion = requests.post("http://172.16.103.38:5509", data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE Oficina
0.Regresar al menu principal
1.Guardar un nuevo empleado
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postOficina(), tablefmt="grid"))
                input("Presione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break