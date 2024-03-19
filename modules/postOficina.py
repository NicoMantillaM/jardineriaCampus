import os
from tabulate import tabulate
import json
import requests
import re
import modules.getOficina as gOfi

#json-server storage/oficina.json -b 5509
# "codigo_oficina": int(input("Ingrese el codigo del oficina : ")),
#         "ciudad": input("Ingrese la ciudad de la oficina: "),
#         "pais": input("Ingrese el pais de la oficina: "),
#         "region": input("Ingrese la region de la oficina: "),
#         "codigo_postal": input("Ingrese el codigo postal: ") ,
#         "telefono": input("Ingrese el telefono de la oficina: "),
#         "linea_direccion1": input("Ingrese la direccion #1 de la oficina: "),
#         "linea_direccion2": input("Ingrese la direccion #2 de la oficina: ")

def postOficina():
    oficina = dict()
    while True:
        try:
            if not oficina.get("codigo_oficina"):    
                codigOfici = input("Ingrese el codigo de oficina (Eje: MAD-ES): ")
                if re.match(r'^([A-Za-z][^\s]*\s*)+$', codigOfici) is not None:
                    oficina["codigo_oficina"]=codigOfici
                else:
                    raise Exception ("El codigo de oficina no cumple con el estandar, intentelo denuevo")

            if not oficina.get("ciudad"):
                ciudad = input("Ingrese la ciudad de la oficina (Eje: Madrid): ")
                if re.match(r'^([A-Za-z]\s*)+$', ciudad) is not None:
                    oficina["ciudad"]=ciudad
                else:
                    raise Exception ("La ciudad de la oficina no cumple con el estandar, intentelo denuevo")
                
            if not oficina.get("pais"):
                pais = input("Ingrese el pais de la oficina (Eje: España): ")
                if re.match(r'^([A-Za-z]\s*)+$', pais) is not None:
                    oficina["pais"]=pais
                else:
                    raise Exception ("El pais de la oficina no cumple con el estandar, intentelo denuevo") 
                
            if not oficina.get("region"):
                region = input("Ingrese la region de la oficina (Eje: Barcelona): ")
                if re.match(r'^([A-Za-z]\s*)+$', region) is not None:
                    oficina["region"]=region
                else:
                    raise Exception ("La region de la oficina no cumple con el estandar, intentelo denuevo")   

            if not oficina.get("codigo_postal"):
                codigoPostal = input("Ingrese el codigo postal (Eje: 28942): ")
                if re.match(r'^[A-Z0-9\s-]+$', codigoPostal) is not None:
                    oficina["codigo_postal"]=codigoPostal
                else:
                    raise Exception ("El codigo Postal de la oficina no cumple con el estandar, intentelo denuevo")

            #Esta expresión regular valida números en varios formatos, incluyendo aquellos sin prefijo internacional y aquellos con prefijos internacionales seguidos de uno a tres bloques de dígitos separados por espacios opcionales.
                
            if not oficina.get("telefono"):
                telefono = input("Ingrese el telefono de la oficina (Eje: 655983045 o 34916540145): ")
                if re.match(r'^\+?\d{1,3}(?: ?\d{2,4}){1,3}$', telefono) is not None:
                    data= gOfi.getAllOficinalefono(telefono)
                    if(data): 
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El telefono de la oficina ya existe")
                    else:
                        oficina["telefono"]=telefono
                else:
                    raise Exception ("El telefono de la oficina no cumple con el estandar, intentelo denuevo")
            
            
            #Esta expresión regular asegura que todas las palabras en la cadena comiencen con una letra mayúscula y respeten los espacios entre ellas, mientras permite diferentes tipos de caracteres en cualquier parte de la cadena excepto al inicio.
                
            if not oficina.get("linea_direccion1"):
                lineaDireccion1 = input("Ingrese la direccion #1 de la oficina (Eje: Calle 10): ")
                if re.match(r'^[A-Z][^\s]*((?:\s+[A-Z][^\s]*)*)$', lineaDireccion1) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion #1 de la oficina ya existe")
                    else:
                        oficina["linea_direccion1"]=lineaDireccion1
                else:
                    raise Exception ("La direccion #1 de la oficina no cumple con el estandar, intentelo denuevo")
            
            if not oficina.get("linea_direccion2"):
                lineaDireccion2 = input("Ingrese la direccion #2 de la oficina (Eje: Calle 10): ")
                if re.match(r'^[A-Z][^\s]*((?:\s+[A-Z][^\s]*)*)$', lineaDireccion2) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion #2 de la oficina ya existe")
                    else:
                        oficina["linea_direccion2"]=lineaDireccion2
                        break

                else:
                    raise Exception ("La direccion #2 de la oficina no cumple con el estandar, intentelo denuevo")
        
        except Exception as error:
            print('-ERROR-')
            print(error)
        
    

    peticion = requests.post("http://172.16.103.18:5509", data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system ("clear")
        print ("""
ADMINISTRAR DATOS DE OFICINA
0.Regresar al menu principal
1.Guardar una nueva oficina
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postOficina(), tablefmt="github"))
                input("Presione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break