import os
from tabulate import tabulate
import requests

def getAllDataEmpleado():
  #json-server storage/empleado.json -b 5508
  peticion=requests.get("http://172.16.103.18:5508")
  data= peticion.json()
  return data


def getAllNombresPuesto(puesto):
    for val in getAllDataEmpleado():
        if val.get("puesto") == puesto:
            return [val]  

def getOneEmpleadocodigo(codigo):
    for val in getAllDataEmpleado():
        if (val.get("codigo_empleado") == codigo):
            return val

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail= []
    for val in getAllDataEmpleado():
       if (val.get("codigo_jefe") == codigo):
           nombreApellidoEmail.append(
               {
                   "nombre": val.get("nombre"),
                   "apellidos": f'{val.get ("apellido1")}{val.get("apellido2)")}',
                   "email": val.get("email"),
                   "jefe": val.get("codigo_jefe")
               }

           )
    return nombreApellidoEmail 

#filtro 4
def getAllNomApeJefeEmpresa():
    nombreApellidoEmailJefeEmpresa = []
    
    for val in getAllDataEmpleado():
        if (val.get ("codigo_jefe") == None ): 
            nombreApellidoEmailJefeEmpresa.append({

                'nombre': val.get('nombre'),
                'apellidos': f'{val.get("apellido1")} {val.get("apellido2")}',
                'email': val.get('email'),
                'puesto': val.get ('puesto'),
                'jefe': val.get('codigo_jefe'),
            }
            )
    return nombreApellidoEmailJefeEmpresa


#filtro 5
def getAllNomApePuestoVec():
    nombreApellidoPuesto=[]
    for val in getAllDataEmpleado():
         if (val.get("puesto") != ("Representante Ventas")):
              nombreApellidoPuesto.append(
               {
                   "nombre": val.get("nombre"),
                   "apellidos": f'{val.get ("apellido1")}{val.get("apellido2)")}',
                   "puesto": val.get("puesto")
               }

           )
    return nombreApellidoPuesto

def menu():
    while True:
        os.system ("clear")
        
        print("""
Reportes de los empleados             
0.Regresar a menu principal
1.Obtener la informacion del jefe por su codigo
2.Obtener el nombre, apellidos y email del jefe de la empresa
3.Obtener el nombre, apellidos y puesto de aquellos empleados que no sean Representantes de ventas
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        try:
            opcion = int(input("\nSeleccione una de las opciones:"))
            if(opcion == 1):
                codigo=int(input("\nIngrese el codigo de jefe: " ))
                print(tabulate(getAllNombreApellidoEmailJefe(codigo),tablefmt="grid"))
                input("Presione una tecla para continuar..........")
            elif(opcion == 2):
                print(tabulate(getAllNomApeJefeEmpresa(),tablefmt="grid"))
                input("Presione una tecla para continuar..........")
            elif(opcion == 3):
                print(tabulate(getAllNomApePuestoVec(),tablefmt="grid"))
                input("Presione una tecla para continuar.....")
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            print("saliendo...")
            break
