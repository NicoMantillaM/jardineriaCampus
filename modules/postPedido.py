import os
import requests
import json
from tabulate import tabulate
import re
import modules.getClients as gCli

#json-server storage/pedido.json -b 55010
# {
#         "codigo_pedido":int(input("Ingrese el codigo del pedido: ")),
#         "fecha_pedido": input("Ingrese la fecha del pedido: "),
#         "fecha_esperada": input("Ingrese la fecha esperada del pedido: "),
#         "fecha_entrega": input("Ingrese la fecha de entrega del pedido: "),
#         "estado": input("Ingrese el estado del pedido (eje: Entregado, Rechazado) : "),
#         "comentario": input("Ingrese un comentario del pedido: "),
#         "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
#     }

def postPedido():
    
    pedido = dict()
    while True:
        try:
            if not pedido.get("codigo_pedido"):
                codigo = input("Ingrese el codigo del cliente (Eje:40): ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    data= gCli.getOneClientcodigo(codigo)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo del cliente ya existe")
                    else:
                        pagos["codigo_cliente"]=codigo
                else:
                    raise Exception("El codigo no cumple con el estandar, intentelo denuevo")

            #Esta expresión regular garantiza que la palabra comience con una letra mayúscula ([A-Z]) y puede tener cualquier combinación de letras mayúsculas y minúsculas en cualquier posición de la palabra. 


            if not pagos.get("forma_pago"):
                formaPa =  input("Ingrese la forma de pago (Eje: PayPal - Transferencia-  Cheque): ")
                if re.match(r'^[A-Z][a-zA-Z0-9-\s]*$', formaPa) is not None:
                    data= gPa.getAllFormasPago(formaPa)
                    if(data):
                        pagos["forma_pago"]=formaPa
                    else:
                        raise Exception("La forma de pago no esta disponible, intentelo denuevo")
                
                else:
                    raise Exception("La forma de pago no cumple con el estandar, intentelo denuevo")
            
            if not pagos.get("id_transaccion"):
                idTrans = input("Ingrese el id de su transaccion (Eje: ak-std-000025)  : ")
                if re.match(r'^[a-z]{2}-[a-z]{3}-\d{6}$', idTrans) is not None:
                    data = gPa.getAllIdTrans(idTrans)
                    if data:
                        raise Exception("El Id de transaccion ya existe.")
                    else:
                        pagos["id_transaccion"] = idTrans
                else:
                    raise Exception("El Id no cumple con el estandar, intentelo denuevo")
                
            if not pagos.get("fecha_pago"):
                fechaPa = input("Ingrese la fecha de pago (Eje: 2009-01-16  ): ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaPa)is not None:
                    pagos["fecha_pago"] = fechaPa
                else:
                    raise Exception("La fecha de pago no cumple con el estandar, intentelo denuevo")
            
            if not pagos.get("total"):
                total = input("Ingrese el total del pago: ")
                if re.match(r'^[0-9]+$', total) is not None:
                    total = int(total)
                    pagos["total"] = total
                    break
                else:
                    raise Exception("El total del pago no cumple con el estandar, intentelo denuevo")
                
        except Exception as error:
            print('-ERROR-')
            print(error)




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