import os
from tabulate import tabulate
import json
import requests

def postPago():
    #json-server storage/pago.json -b 5507
    pagos = { 
      
        "codigo_cliente": int(input("Ingrese el codigo del cliente : ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese el id de transaccion: "),
        "fecha_pago": input("Ingrese la fecha de pago: "),
        "total": int(input("Ingrese el total del pago : "))
    }

    peticion = requests.post("http://192.168.1.11:55011", data=json.dumps(pagos))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE LOS PAGOS
0.Regresar al menu principal
1.Guardar un nuevo pago
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postPago(), tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break