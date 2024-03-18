import os
from tabulate import tabulate
import json
import requests
import re
import modules.getEmpleado as gEmp

    # #json-server storage/empleado.json -b 5508
    # empleado = {
    #     "codigo_empleado": int(input("Ingrese el codigo del empleado : ")),
    #     "nombre": input("Ingrese el nombre del empleado: "),
    #     "apellido1": input("Ingrese el apellido 1 del empleado: "),
    #     "apellido2": input("Ingrese el apellido 2 del empleado: "),
    #     "extension": input("Ingrese la extension del empleado: "),
    #     "email": input("Ingrese el email del empleado: "),
    #     "codigo_oficina": input("Ingrese el codigo de oficina: "),
    #     "codigo_jefe": input("Ingrese el codigo de jefe: "),
    #     "puesto": input("Ingrese el puesto: ")
    # }

    # peticion = requests.post("http://172.16.103.38:5508", data=json.dumps(empleado))
    # res = peticion.json()
    # res["Mensaje"]= "Producto Guardado"
    # return [res]

def postEmpleado():
    empleado = dict()
    while True:
        try:
            if not empleado.get("codigo_empleado"):
                codigoEmp = input("Ingrese el codigo del empleado (Eje:19): ")
                if re.match(r'^[0-9]+$', codigoEmp) is not None:
                    codigoEmp = int(codigoEmp)
                    data= gEmp.getOneEmpleadocodigo(codigoEmp)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo del empleado ya existe")
                    else:
                        empleado["codigo_empleado"]=codigoEmp
                else:
                    raise Exception("El codigo no cumple con el estandar, intentelo denuevo")


                if not empleado.get("nombre"):
                    nombre = input("Ingrese el nombre del empleado (Eje:Marco): ")
                    if re.match(r'^([A-Za-z][^\s]*\s*)+$', nombre) is not None:
                        empleado["nombre"]=nombre   
                else:
                    raise Exception ("El nombre del cliente no cumple con el estandar, intentelo denuevo") 

                if not empleado.get("apellido1"):
                    apellido1 = input("Ingrese el apellido 1 del empleado: (Eje:Soria): ")
                    if re.match(r'^([A-Za-z]\s*)+$', apellido1) is not None:
                        empleado["apellido1"]=apellido1
                else:
                    raise Exception ("El apellido #1 del empleado no cumple con el estandar, intentelo denuevo")
                
                if not empleado.get("apellido2"):
                    apellido2 = input("Ingrese el apellido 2 del empleado: (Eje:Carrasco): ")
                    if re.match(r'^([A-Za-z]\s*)+$', apellido2) is not None:
                        empleado["apellido2"]=apellido2
                else:
                    raise Exception ("El apellido #2 del empleado no cumple con el estandar, intentelo denuevo")
                
                if not empleado.get("extension"):
                    extension = input("Ingrese la extension del empleado (Eje:2899): ")
                    if re.match(r'^\d{4}$', extension) is not None: 
                        empleado["extension"]=extension

                    else:
                        raise Exception ("La extension del empleado no cumple con el estandar, intentelo denuevo")
                    
                if not empleado.get("email"):
                    email = input("Ingrese el email del empleado (Eje: asoria@jardineria.es): ")
                    if re.match(r'^([A-Za-z][^\s]*\s*)+$', email) is not None:
                        empleado["email"]=email
                else:
                    raise Exception ("El email del empleado no cumple con el estandar, intentelo denuevo")

                if not empleado.get("codigo_oficina"):    
                    codigOfi = input("Ingrese el codigo de oficina (Eje: MAD-ES): ")
                    if re.match(r'^([A-Za-z][^\s]*\s*)+$', codigOfi) is not None:
                        empleado["codigo_oficina"]=codigOfi
                else:
                    raise Exception ("El codigo de oficina no cumple con el estandar, intentelo denuevo")
                
                #Esta expresión regular valida códigos de oficina que constan de tres letras mayúsculas seguidas de un guion medio y luego dos o tres letras mayúsculas más. 
            
                if not empleado.get("codigo_jefe"):    
                    codigoJef = input("Ingrese el codigo de jefe: (Eje: 34): ")
                    if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigoJef) is not None:
                        codigoJef = int(codigoJef)
                        empleado["codigo_jefe"]=codigoJef
                else:
                    raise Exception ("El codigo del jefe no cumple con el estandar, intentelo denuevo")
                
                #Esta expresión regular asegura que la cadena comience con una palabra que comience con mayúscula, seguida de una o más letras, seguida de uno o más espacios en blanco, y luego otra palabra que comience con mayúscula.

                if not empleado.get("puesto"):    
                    puesto = input("Ingrese el puesto: (Eje: Director Oficina): ")
                    if re.match(r'^[A-Z][a-zA-Z]*\s+[A-Z][a-zA-Z]*$', puesto) is not None:
                        data= gEmp.getAllNombresPuesto(puesto)
                        if(data):
                            empleado["puesto"]=puesto
                            
                            break
                        
                        else:
                            raise Exception("El puesto ingresado no esta disponible, intentelo denuevo")
                    
                    else:
                        raise Exception ("El puesto del empleado no cumple con el estandar, intentelo denuevo")

        except Exception as error:
            print('-ERROR-')
            print(error)    


    peticion = requests.post("http://192.168.1.11:5508", data=json.dumps(empleado))
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