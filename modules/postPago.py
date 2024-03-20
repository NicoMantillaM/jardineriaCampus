import os
from tabulate import tabulate
import json
import requests
import re
import modules.getClients as gCli
import modules.getPago as gPa
#json-server storage/pago.json -b 5507
 #     "codigo_cliente": int(input("Ingrese el codigo del cliente : ")),
    #     "forma_pago": input("Ingrese la forma de pago: "),
    #     "id_transaccion": input("Ingrese el id de transaccion: "),
    #     "fecha_pago": input("Ingrese la fecha de pago: "),
    #     "total": int(input("Ingrese el total del pago : "))
    # }

def postPago():
    pagos = dict()
    while True:
        try:
            if not pagos.get("codigo_cliente"):
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

    peticion = requests.post("http://154.38.171.54:5006/pagos", data=json.dumps(pagos))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def deleteCliente(id):
    data = gCli.getClienteCodigo(id)
    if(len(data)):

        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "message": "producto no encontrado",
                    "id": id
            }],
            "status": 400,
        }

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