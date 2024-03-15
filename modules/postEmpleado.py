import os
from tabulate import tabulate
import json
import requests

def postEmpleado():
    #json-server storage/empleado.json -b 5508
    empleado = {
        "codigo_empleado": int(input("Ingrese el codigo del cliente : ")),
        "nombre": input("Ingrese el nombre del empleado: "),
        "apellido1": input("Ingrese el apellido 1 del empleado: "),
        "apellido2": input("Ingrese el apellido 2 del empleado: "),
        "extension": input("Ingrese la extension del empleado: "),
        "email": input("Ingrese el email del empleado: "),
        "codigo_oficina": input("Ingrese el codigo de oficina: "),
        "codigo_jefe": input("Ingrese el codigo de jefe: "),
        "puesto": input("Ingrese el puesto: ")
    }

    peticion = requests.post("http://172.16.103.38:5508", data=json.dumps(empleado))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE EMPLEADOS
0.Regresar al menu principal
1.Guardar un nuevo empleado
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postEmpleado(), tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break