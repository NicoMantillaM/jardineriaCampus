import os
import requests
import json
from tabulate import tabulate

def postPedido():
    #json-server storage/pedido.json -b 55010
    pedido = {
        "codigo_pedido":int(input("Ingrese el codigo del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha esperada del pedido: "),
        "fecha_entrega": input("Ingrese la fecha de entrega del pedido: "),
        "estado": input("Ingrese el estado del pedido (eje: Entregado, Rechazado) : "),
        "comentario": input("Ingrese un comentario del pedido: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
    }

    peticion = requests.post("http://192.168.1.11:55010", data= json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE LOS PEDIDOS
0.Regresar al menu principal
1.Guardar un nuevo pedido
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postPedido(), tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break