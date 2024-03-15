import os
from tabulate import tabulate
import requests

def getAllDataClient():
  #json-server storage/cliente.json -b 5507
  peticion=requests.get("http://192.168.1.11:5507")
  data= peticion.json()
  return data

def getAllDataEmpleado():
 #json-server storage/empleado.json -b 5508
  peticion=requests.get("http://192.168.1.11:5508")
  data= peticion.json()
  return data 


def getAllClientesName():
  clienteName= list()
  for val in getAllDataClient():
    codigoName= dict({ 
      "codigo_cliente": val.get("codigo_cliente"),
      "nombre_cliente": val.get("nombre_cliente")
     })
    clienteName.append(codigoName)
  return clienteName

def getOneClientcodigo(codigo):
  for val in getAllDataClient():
    if (val.get("codigo_cliente")== codigo):
      return [{ 
      "codigo_cliente": val.get("codigo_cliente"),
      "nombre_cliente": val.get("nombre_cliente")
     }]

def getAllClientCreditCiudad(limite_credit, ciudad):
  clienteCredic= list()
  for val in getAllDataClient():
   if (val.get("limite_credito") >= limite_credit and val.get("ciudad") == ciudad):
      clienteCredic.append({
        "Codigo": val.get("codigo_cliente"),
        "Nombre del  Cliente": val.get("nombre_cliente"),
        "Director":f"{val.get('nombre_contacto')} {val.get('nombre_contacto')}",
        "Telefono":val.get('telefono'),
        "Fax":val.get('fax'),
        "Direcciones":f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
        "Origen":f"{val.get('pais')} {val.get('region')}{val.get('ciudad')}{val.get('codigo_postal')}",
        "Codigo del asesor":{val.get('codigo_empleado_rep_ventas')},
        "Credito":val.get('limite_credito')
      })
  return clienteCredic


def getAllClientPaisRegionCiudad (pais,region=None, ciudad=None):
  clientZone= list()
  for val in getAllDataClient():
    if(
     val.get("pais")== pais or
     (val.get("region")== region or val.get("region") == None) and
     (val.get("ciudad")== ciudad or val.get("ciudad") == None)
    ):
      clientZone.append(val)
  return  clientZone  

def getAllClientCiudad (ciudad):
  clienteCiud= list()
  for val in getAllDataClient():
    if(
     (val.get("ciudad")== ciudad or val.get("ciudad") == None)
    ):
      clienteCiud.append(val)
  return  clienteCiud

def getAllClientDireccion1():
  clientDireccion1= list()
  for val in getAllDataClient():
    direccion1= dict({ 
    "codigo_cliente": val.get("codigo_cliente"),
    "nombre_cliente": val.get("nombre_cliente"),
    "linea_direccion1": val.get("linea_direccion1")
    })
    clientDireccion1.append(val)
  return clientDireccion1

def getOneClienttelefono(telefono):
  for val in getAllDataClient():
    if (val.get("telefono")== telefono):
      return [{
      "codigo_cliente": val.get("codigo_cliente"),
      "nombre_cliente": val.get("nombre_cliente")
      }]
 

def getAllClientCreditEntre():
  clientCredit= list()
  for val in getAllDataClient():
   if(val.get("limite_credito")>= 5000 and val.get("limite_credito") <= 10000):
      clientCredit.append(val)
  return  clientCredit

def getAllClientFax():
  clientFax= list()
  for val in getAllDataClient():
    fax= dict({
      "nombre_cliente": val.get("nombre_cliente"),
      "fax":  val.get("fax")
    })
    clientFax.append(val)
  return clientFax

#filtro 6
def getAllClientsPais():
  paiscliente= []
  for val in getAllDataClient():
    if (val.get("pais")==("Spain")):
      paiscliente.append(
        {
         "nombre": val.get("nombre_cliente"),
         "pais": val.get("pais")
        }
      )
  return paiscliente
#filtro 16
def getAllCiudadCodigo():
  codigoCiudad= []
  for val in getAllDataClient():
    if val.get("ciudad")== "Madrid":
      if val.get("codigo_empleado_rep_ventas")== 11 or val.get("codigo_empleado_rep_ventas")== 30:
        codigoCiudad.append({
          "codigo_cliente": val.get("codigo_cliente"),
          "nombre_cliente": val.get("nombre_cliente"),
          "ciudad": val.get("ciudad"),
          "codigo_empleado_rep_ventas": val.get("codigo_empleado_rep_ventas")
    })
  return codigoCiudad

def getAllClientsRepre():
  clientesRepre= []
  for val in getAllDataClient():
    for val2 in getAllDataEmpleado():
      if val.get("codigo_empleado_rep_ventas")== val2.get("codigo_empleado") and val2.get ("puesto")== ("Representante Ventas"):
       clientesRepre.append(
         {
         "codigo_cliente": val.get("codigo_cliente"),
         "nombre_cliente": val.get("nombre_cliente"),
         "nombre": val2.get("nombre"),
         "apellido": f"{val2.get('apellido1')} {val2.get('apellido2')}"
         }
        )
  return clientesRepre
    

def menu():
  while True:
    os.system ("clear")
    print(""" 
        
Reportes de los clientes
0.Regresar al menu principal
1.Obtener todos los clientes (codigo y nombre)
2.Obtener un cliente por su codigo(codigo y su nombre)
3.Obtener toda la informacion de un cliente segun su limite de credito y ciudad
4.Obtener todos los clientes que cuenten con un limite de credito entre 5000 y 10000 
5.Obtener un cliente por su telefono (codigo, nombre)
6.Obtener todos los clientes de la ciudad de madrid junto con sus representantes de ventas que tengan su codigo en 11 o 30
7.Obtener el nombre de todos los clientes junto con el nombre y los apellidos de sus representantes de ventas 
  -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
    try:
      opcion = int(input("\nSeleccione una de las opciones:"))
      if(opcion == 1):
        print(tabulate(getAllClientesName(),tablefmt="grid"))
      elif(opcion == 2):
          #try: 
            codigo= int(input("Ingrese el codigo del cliente: "))
            print(tabulate(getOneClientcodigo(codigo),tablefmt="grid"))
          #except KeyboardInterrupt:
            #return menu()
      elif(opcion == 3):
        #try:
          clienteCredic= float(input("\nIngrese el limite de credito: "))
          ciudad= str(input("\n Ingrese la ciudad"))
          print(tabulate(getAllClientCreditCiudad(clienteCredic,ciudad),tablefmt="grid"))
        #except KeyboardInterrupt:
          #return menu()
      elif(opcion == 4):
        print(tabulate(getAllClientCreditEntre(),tablefmt="grid"))
      elif(opcion == 5):
        telefono= str(input("\nIngrese el telefono del cliente: "))
        print(tabulate(getOneClienttelefono(telefono),tablefmt="grid"))
      elif(opcion == 6):
        print(tabulate(getAllCiudadCodigo(),tablefmt="grid"))
      elif(opcion == 7):
        print(tabulate(getAllClientsRepre(),tablefmt="grid"))  
        input("Precione una tecla para continuar.....")
      elif(opcion == 0):
        break
    except KeyboardInterrupt:
      break


    #try:
      #entrada = input("Ingresa Ctrl + c para ir a menu anterior: ")
    # Aquí puedes hacer lo que necesites con la entrada
      #print("Entrada recibida:", entrada)
    #except KeyboardInterrupt:
      #return menu()
      
      