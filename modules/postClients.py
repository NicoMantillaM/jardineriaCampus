import os
from tabulate import tabulate
import json
import requests
import modules.getClients as gCli
import modules.getGamas as gGa
import re


    #json-server storage/cliente.json -b 5507
    #     "codigo_cliente": int(input("Ingrese el codigo del cliente : ")),
    #     "nombre_cliente": input("Ingrese el nombre del cliente: "),
    #     "nombre_contacto": input("Ingrese el nombre del contacto: "),
    #     "apellido_contacto": input("Ingrese el apellido del contacto: "),
    #     "telefono": input("Ingrese el telefono del cliente : "),
    #     "fax": input("Ingrese el fax  del cliente : "),
    #     "linea_direccion1": input("Ingrese la direccion #1 del cliente : "),
    #     "linea_direccion2":input("Ingrese la direccion #2 del cliente : "),
    #     "ciudad": input("Ingrese la ciudad del cliente : "),
    #     "region": input("Ingrese la region del cliente : "),
    #     "pais": input("Ingrese el pais del cliente : "),
    #     "codigo_postal": input("Ingrese el codigo postal del cliente : "),
    #     "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del representante de ventas : ")),
    #     "limite_credito": int(input("Ingrese el limite del credito: "))
    # }

    # peticion = requests.post("http://172.16.103.38:5507", data=json.dumps(cliente))
    # res = peticion.json()
    # res["Mensaje"]= "Producto Guardado"
    # return [res]

def postClients():
    cliente = dict()
    while True:
        try:
            if not cliente.get("codigo_cliente"):
                codigo = input("Ingrese el codigo del cliente (Eje:40): ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    data= gCli.getOneClientcodigo(codigo)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo del cliente ya existe")
                    else:
                        cliente["codigo_cliente"]=codigo
                else:
                    raise Exception("El codigo no cumple con el estandar, intentelo denuevo")


            # expresión regular que contiene palabras donde la primera letra puede ser cualquier letra mayúscula o minúscula, seguida de cualquier secuencia de caracteres (excluyendo espacios), y se repite una o más veces, con espacios opcionales entre las palabras.
                
            if not cliente.get("nombre_cliente"):
                nombre = input("Ingrese el nombre del cliente (Eje:Maria Jose): ")
                if re.match(r'^([A-Za-z][^\s]*\s*)+$', nombre) is not None:
                    cliente["nombre_cliente"]=nombre   
                else:
                    raise Exception ("El nombre del cliente no cumple con el estandar, intentelo denuevo") 
            
            #expresión regular que verifica si todas las palabras en una cadena comienzan con una letra mayúscula y respetan los espacios entre ellas.
                
            if not cliente.get("nombre_contacto"):
                nombreContac = input("Ingrese el nombre de contacto del cliente (Eje:Daniel): ")
                if re.match(r'^([A-Za-z]\s*)+$', nombreContac) is not None:
                    cliente["nombre_contacto"]=nombreContac
                else:
                    raise Exception ("El nombre de contacto del cliente no cumple con el estandar, intentelo denuevo")
                
            #esta expresión regular aceptará palabras que comiencen con una letra mayúscula o minúscula seguida opcionalmente de espacios en blanco.

            if not cliente.get("apellido_contacto"):
                apellidoContac = input("Ingrese el apellido de contacto del cliente (Eje:Martinez): ")
                if re.match(r'^([A-Za-z]\s*)+$', apellidoContac) is not None:
                    cliente["apellido_contacto"]=apellidoContac
                else:
                    raise Exception ("El apellido de contacto del cliente no cumple con el estandar, intentelo denuevo")
            
            #esta expresión regular verificará si numero_telefono Comienza con uno a tres dígitos para el código de país. Luego, permite un espacio opcional y acepta números con o sin guiones, seguidos de otros números opcionales.
                
            if not cliente.get("telefono"):
                telefono = input("Ingrese el telefono del cliente (Eje: 655983045 o 34916540145): ")
                if re.match(r'^\d{1,3}(?: ?\d{4}-?\d{4}|\s?\d{6,11})$', telefono) is not None:
                    data= gCli.getOneClienttelefono(telefono)
                    if(data): 
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El telefono del cliente ya existe")
                    else:
                        cliente["telefono"]=telefono
                else:
                    raise Exception ("El telefono del cliente no cumple con el estandar, intentelo denuevo")
                
            if not cliente.get("fax"):
                fax = input("Ingrese el fax del cliente (Eje: 212343222 o 2 8005-7162): ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', fax) is not None: 
                    cliente["fax"]=fax
                    
                else:
                    raise Exception ("El fax del cliente no cumple con el estandar, intentelo denuevo")
            
            #Esta expresión regular asegura que todas las palabras en la cadena comiencen con una letra mayúscula y respeten los espacios entre ellas, mientras permite diferentes tipos de caracteres en cualquier parte de la cadena excepto al inicio.
                
            if not cliente.get("linea_direccion1"):
                lineaDireccion1 = input("Ingrese la direccion #1 del cliente (Eje: Calle 10): ")
                if re.match(r'^[A-Z][^\s]*((?:\s+[A-Z][^\s]*)*)$', lineaDireccion1) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion #1 del cliente ya existe")
                    else:
                        cliente["linea_direccion1"]=lineaDireccion1
                else:
                    raise Exception ("La direccion #1 del cliente no cumple con el estandar, intentelo denuevo")
            
            if not cliente.get("linea_direccion2"):
                lineaDireccion2 = input("Ingrese la direccion #2 del cliente (Eje: Calle 10): ")
                if re.match(r'^[A-Z][^\s]*((?:\s+[A-Z][^\s]*)*)$', lineaDireccion2) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion #2 del cliente ya existe")
                    else:
                        cliente["linea_direccion2"]=lineaDireccion2
                else:
                    raise Exception ("La direccion #2 del cliente no cumple con el estandar, intentelo denuevo")
                
            if not cliente.get("ciudad"):
                ciudad = input("Ingrese la ciudad del cliente (Eje: Madrid): ")
                if re.match(r'^([A-Za-z]\s*)+$', ciudad) is not None:
                    cliente["ciudad"]=ciudad
                else:
                    raise Exception ("La ciudad del cliente no cumple con el estandar, intentelo denuevo")
                
            if not cliente.get("region"):
                region = input("Ingrese la region del cliente (Eje: Barcelona): ")
                if re.match(r'^([A-Za-z]\s*)+$', region) is not None:
                    cliente["region"]=region
                else:
                    raise Exception ("La region del cliente no cumple con el estandar, intentelo denuevo")
                
            if not cliente.get("pais"):
                pais = input("Ingrese el pais del cliente (Eje: España): ")
                if re.match(r'^([A-Za-z]\s*)+$', pais) is not None:
                    cliente["pais"]=pais
                else:
                    raise Exception ("El pais del cliente no cumple con el estandar, intentelo denuevo")
            
            #Esta expresión regular valida códigos postales que contienen entre 5 y 7 dígitos, permitiendo así que los códigos postales ingresados tengan hasta 7 dígitos

            if not cliente.get("codigo_postal"):
                codigoPostal = input("Ingrese el codigo postal (Eje: 28942): ")
                if re.match(r'^\d{5,7}$', codigoPostal) is not None:
                    cliente["codigo_postal"]=codigoPostal
                else:
                    raise Exception ("El codigo Postal del cliente no cumple con el estandar, intentelo denuevo")
                
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigoVent = input("Ingrese el codigo del representante de ventas: (Eje: 42): ")
                if re.match(r'^[0-9]+$', codigoVent) is not None:
                    codigoVent = int(codigoVent)
                    cliente["codigo_empleado_rep_ventas"]=codigoVent
                else:
                    raise Exception ("El codigo del empleado no cumple con el estandar, intentelo denuevo")
            
            #expresión regular valida códigos postales que pueden tener cualquier número de dígitos antes del punto decimal, y opcionalmente, pueden tener dígitos adicionales después del punto decimal.

            if not cliente.get("limite_credito"):
                limiteCre = input("Ingrese el limite de credito: (Eje: 6000.0): ")
                if re.match(r'^\d+(\.\d+)?$', limiteCre) is not None:
                    limiteCre = float(limiteCre)
                    cliente["limite_credito"]=limiteCre

                    break


                else:
                    raise Exception ("El codigo del empleado no cumple con el estandar, intentelo denuevo")
                
        except Exception as error:
            print('-ERROR-')
            print(error)        

    peticion = requests.post("http://172.16.103.18:5507", data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def deleteCliente(id):
    data = gCli.getClienteCodigo(id)
    if(len(data)):

        peticion = requests.delete(f"http://172.16.103.18:5507/clientes/{id}")
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
    
def updateCliente(id):
    data= gCli.getClienteCodigo(id)
    if(len(data)):
            clientes=dict()
            while True:
                try:
                    if(not clientes.get("codigo_cliente")):
                        codigo_cliente=input("Ingrese el codigo del cliente: ")
                        if(re.match(r'^[0-9]+$',codigo_cliente)is not None):
                            codigo_cliente= int(codigo_cliente)
                            data=gCli.getClienteCodigo2(codigo_cliente)
                            if(data):
                                print(tabulate(data,tablefmt="grid"))
                                raise Exception("El codigo ya pertenece a un cliente")
                            else:
                                clientes["codigo_cliente"]=codigo_cliente
                        else:
                            raise Exception("El codigo del cliente no cumple con el estandar establecido")
                    
                    if(not clientes.get("nombre_cliente")):
                        nombre_cliente=input("Ingrese el nombre del cliente: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre_cliente)is not None):
                            clientes["nombre_cliente"]=nombre_cliente
                        else:
                            raise Exception("El nombre del producto no cumple con el estandar establecido")

                    if(not clientes.get("nombre_contacto")):
                        nombre_contacto=input("Ingrese su nombre: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre_contacto)is not None):
                            clientes["nombre_contacto"]=nombre_contacto
                        else:
                            raise Exception("Su nombre no cumple con el estandar establecido") 

                    if(not clientes.get("apellido_contacto")):
                        apellido_contacto=input("Ingrese sus apellidos: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',apellido_contacto)is not None):
                            clientes["apellido_contacto"]=apellido_contacto
                        else:
                            raise Exception("Sus apellidos no cumplen con el estandar establecido")   

                    if(not clientes.get("telefono")):
                        telefono=input("Ingrese su telefono: ")
                        if(re.match(r'^[0-9]{9,11}$',telefono)is not None):
                            telefono= int(telefono)
                            clientes["telefono"]=telefono
                        else:
                            raise Exception("Su telefono no cumple con el estandar establecido")  

                    if(not clientes.get("fax")):
                        fax=input("Ingrese su fax: ")
                        if(re.match(r'^[0-9]{9,11}$',fax)is not None):
                            fax= int(fax)
                            clientes["fax"]=fax
                        else:
                            raise Exception("Su fax no cumple con el estandar establecido")   

                    if(not clientes.get("linea_direccion1")):
                        linea_direccion1=input("Ingrese su direccion principal: ")
                        if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion1)is not None):
                            clientes["linea_direccion1"]=linea_direccion1
                        else:
                            raise Exception("Su linea de direccion principal no cumple con el estandar establecido")   
                    
                    if(not clientes.get("linea_direccion2")):
                        linea_direccion2=input("Ingrese su direccion principal: ")
                        if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion2)is not None):
                            clientes["linea_direccion2"]=linea_direccion2
                        else:
                            raise Exception("Su linea de direccion secundaria no cumple con el estandar establecido")   
                    if(not clientes.get("ciudad")):
                        ciudad=input("Ingrese su ciudad: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',ciudad)is not None):
                            clientes["ciudad"]=ciudad
                        else:
                            raise Exception("Su ciudad no cumple con el estandar establecido")  
                    
                
                    if(not clientes.get("codigo_postal")):
                        codigo_postal=input("Ingrese su codigo postal: ")
                        if(re.match(r'^[0-9]{5}$',codigo_postal)is not None):
                            codigo_postal= int(codigo_postal)
                            clientes["codigo_postal"]=codigo_postal
                        else:
                            raise Exception("Su codigo postal no cumple con el estandar establecido")  
                    
                    # if(not clientes.get("codigo_empleado_rep_ventas")):
                    #     codigo_empleado_rep_ventas=input("Seleccione el codigo de su Representante de Ventas:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gGa.getAllCoEmp())]))
                    #     if(re.match(r'^[0-9]$',codigo_empleado_rep_ventas)is not None):
                    #         codigo_empleado_rep_ventas= int(codigo_empleado_rep_ventas)
                    #         codigo_empleado_rep_ventas = gCem.getAllCoEmp()[codigo_empleado_rep_ventas]
                    #         clientes["codigo_empleado_rep_ventas"]=codigo_empleado_rep_ventas
                    #     else:
                    #         raise Exception("El codigo de su Representante no cumple con el estandar establecido")  
                            
                    if(not clientes.get("limite_credito")):
                        limite_credito=input("Ingrese su limite de credito: ")
                        if(re.match(r'^[0-9]{4,5}$',limite_credito)is not None):
                            limite_credito= float(limite_credito)
                            clientes["limite_credito"]=limite_credito
                            break
                        else:
                            raise Exception("Su limite de credito no cumple con el estandar establecido")  
                except Exception as error:
                    print(error)  
            pet=requests.put(f"http://172.16.103.26:5506/clientes/{id}", data=json.dumps(clientes))
            res=pet.json()
            res["Mensaje"] = "Producto Guardado"
            return [res]
    else:
        return[{
            "message": "Producto no encontrado",
            "id": id
            }]   

def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE CLIENTES
0.Regresar al menu principal
1.Guardar un cliente nuevo
2.Eliminar
3.Actualizar
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = input("\nSelecione una de las opciones: ")
            opcion = int(opcion)
            if(opcion == 1):
                print(tabulate(postClients(), tablefmt="grid"))
                input("Precione una tecla para continuar.....")
            if(opcion == 2):
                idClient = input("Ingrese el id del cliente que desea eliminar: ")
                print(tabulate(deleteCliente(idClient)["body"], tablefmt="grid"))
                input("Presione una tecla para continuar......")
            if(opcion == 3):
                idClient = input("Ingrese el id del cliente que desea eliminar: ")
                print(tabulate(updateCliente(idClient), tablefmt="grid"))
                input("Presione una tecla para continuar......")

            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break

