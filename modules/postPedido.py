import os
import requests
import json
from tabulate import tabulate
import re
import modules.getClients as gCli
import modules.getPedido as gPed

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
                codigo = input("Ingrese el codigo del pedido (Eje:105): ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    data= gPed.getPedidoCodigo(codigo)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo del pedido ya existe")
                    else:
                        pedido["codigo_pedido"]=codigo
                else:
                    raise Exception("El codigo no cumple con el estandar, intentelo denuevo")  
                 
            if not pedido.get("fecha_pedido"):
                fechaPed = input("Ingrese la fecha del pedido (Eje: 2007-10-23  ): ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaPed)is not None:
                    pedido["fecha_pedido"] = fechaPed
                else:
                    raise Exception("La fecha del pedido no cumple con el estandar, intentelo denuevo")
                
            if not pedido.get("fecha_esperada"):
                fechaEs = input("Ingrese la fecha esperada del pedido (Eje: 2007-10-23  ): ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEs)is not None:
                    pedido["fecha_esperada"] = fechaEs
                else:
                    raise Exception("La fecha esperada del pedido no cumple con el estandar, intentelo denuevo") 

            if not pedido.get("fecha_entrega"):
                fechaEn = input("Ingrese la fecha de entrega del pedido (Eje: 2007-10-23  ): ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEn)is not None:
                    pedido["fecha_entrega"] = fechaEn
                else:
                    raise Exception("La fecha de entrega del pedido no cumple con el estandar, intentelo denuevo")             
            
            if not pedido.get("estado"):
                estado = input("Ingrese el estado del pedido (eje: Rechazado,Entregado,Pendiente): ")
                if re.match(r'^([A-Za-z]\s*)+$', estado) is not None:
                    pedido["estado"] = estado
                   
                else:
                    raise Exception("El estado del pedido no cumple con el estandar, intentelo denuevo")

            if not pedido.get("comentario"):
                comentario = input("Ingrese un comentario del pedido: ")
                if re.match(r'^[A-Z][^\s]*((?:\s+[A-Z][^\s]*)*)$', comentario) is not None:
                    pedido["comentario"] = comentario
                else:
                    raise Exception("El comentario no cumple con el estandar, intentelo denuevo")
                
            if not pedido.get("codigo_cliente"):
                codigo = input("Ingrese el codigo del cliente (Eje:12): ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    data= gPed.getAllClientecodigo(codigo)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo del cliente ya existe")
                    else:
                        pedido["codigo_cliente"]=codigo
                        break
                else:
                    raise Exception("El codigo no cumple con el estandar, intentelo denuevo")  

        except Exception as error:
            print('-ERROR-')
            print(error)

    peticion = requests.post("http://154.38.171.54:5007/pedidos", data= json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"]= "Pedido Guardado"
    return [res]

def deletePedido(id):
    data = gPed.getPedidoCodigo(id)
    if(len(data)):
        while True:
            try:
                print("""
                ¿Seguro que desea eliminar el pedido?
                      1.Si
                      2.No
                """)
                opcion= (input("Seleccione la opcion Si o No: "))
                if(re.match(r'^[1-2]$', opcion)is not None):
                        opcion=int(opcion)
                        if (opcion==1):
                            peticion = requests.delete(f"http://154.38.171.54:5008/pedidos/{id}")
                            if(peticion.status_code==204):
                                return print("El pedido se elimino efectivamente")
                            break
                        else:
                            return print("El pedido no se eliminara")
                else:
                    raise Exception("La opcion ingresada no cumple con el estandar, recuerda debe ser 1 o 2")
            except Exception as error:
                print(error)  
    else:
        return print("El pedido no fue encontrado, recuerda ingresar un id valido")  

def updatePedido(id):
    data = gPed.getPedidoCodigo(id)
    if(len(data)):
        pedido = dict()
        while True:
            try:
                if not pedido.get("codigo_pedido"):
                    codigo = input("Ingrese el codigo del pedido (Eje:105): ")
                    if re.match(r'^[0-9]+$', codigo) is not None:
                        codigo = int(codigo)
                        data= gPed.getPedidoCodigo(codigo)
                        if(data):
                            print(tabulate(data,tablefmt="grid"))
                            raise Exception("El codigo del pedido ya existe")
                        else:
                            pedido["codigo_pedido"]=codigo
                    else:
                        raise Exception("El codigo no cumple con el estandar, intentelo denuevo")  
                    
                if not pedido.get("fecha_pedido"):
                    fechaPed = input("Ingrese la fecha del pedido (Eje: 2007-10-23  ): ")
                    if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaPed)is not None:
                        pedido["fecha_pedido"] = fechaPed
                    else:
                        raise Exception("La fecha del pedido no cumple con el estandar, intentelo denuevo")
                    
                if not pedido.get("fecha_esperada"):
                    fechaEs = input("Ingrese la fecha esperada del pedido (Eje: 2007-10-23  ): ")
                    if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEs)is not None:
                        pedido["fecha_esperada"] = fechaEs
                    else:
                        raise Exception("La fecha esperada del pedido no cumple con el estandar, intentelo denuevo") 

                if not pedido.get("fecha_entrega"):
                    fechaEn = input("Ingrese la fecha de entrega del pedido (Eje: 2007-10-23  ): ")
                    if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEn)is not None:
                        pedido["fecha_entrega"] = fechaEn
                    else:
                        raise Exception("La fecha de entrega del pedido no cumple con el estandar, intentelo denuevo")             
                
                if not pedido.get("estado"):
                    estado = input("Ingrese el estado del pedido: ")
                    if re.match(r'^([A-Za-z]\s*)+$', estado) is not None:
                            pedido["estado"] = estado
                    else:
                        raise Exception("El estado del pedido no cumple con el estandar, intentelo denuevo")

                if not pedido.get("comentario"):
                    comentario = input("Ingrese un comentario del pedido: ")
                    if re.match(r'^[A-Z][^\s]*((?:\s+[A-Z][^\s]*)*)$', comentario) is not None:
                        pedido["comentario"] = comentario
                    else:
                        raise Exception("El comentario no cumple con el estandar, intentelo denuevo")
                    
                if not pedido.get("codigo_cliente"):
                    codigo = input("Ingrese el codigo del cliente (Eje:12): ")
                    if re.match(r'^[0-9]+$', codigo) is not None:
                        codigo = int(codigo)
                        pedido["codigo_cliente"]=codigo
                        break
                    else:
                        raise Exception("El codigo no cumple con el estandar, intentelo denuevo")  

            except Exception as error:
                print(error)

        peticion = requests.post(f"http://154.38.171.54:5007/pedidos/{id}", data= json.dumps(pedido))
        res = peticion.json()
        res["Mensaje"]= "pedido Guardado"
        return [res]
    else:
        print ("El pedido no existe")
           


def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE LOS PEDIDOS
0.Regresar al menu principal
1.Guardar un nuevo pedido
2.Eliminar un pedido
3.Actualizar un pedido
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postPedido(), tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            if(opcion == 2):
                idClient = input("Ingrese el id del pedido que desea eliminar: ")
                print(tabulate(deletePedido(idClient), tablefmt="grid"))
                input("Presione una tecla para continuar......")
            if(opcion == 3):
                idClient = input("Ingrese el id del pedido que desea actualizar: ")
                print(tabulate(updatePedido(idClient), tablefmt="grid"))
                input("Presione una tecla para continuar......")

            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break