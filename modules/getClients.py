import storage.cliente as cli

from tabulate import tabulate

def getAllClientesName():
  clienteName= list()
  for val in cli.clientes:
    codigoName= dict({ 
      "codigo_cliente": val.get("codigo_cliente"),
      "nombre_cliente": val.get("nombre_cliente")
     })
    clienteName.append(codigoName)
  return clienteName

def getOneClientcodigo(codigo):
  for val in cli.clientes:
    if (val.get("codigo_cliente")== codigo):
      return [{ 
      "codigo_cliente": val.get("codigo_cliente"),
      "nombre_cliente": val.get("nombre_cliente")
     }]

def getAllClientCreditCiudad(limite_credit, ciudad):
  clienteCredic= list()
  for val in cli.clientes:
   if (val.get("limite_credito") >= limite_credit and val.get("ciudad") == ciudad):
      clienteCredic.append({
        "Codigo": val.get("codigo_cliente"),
        "Nombre del  Cliente": val.get("nombre_cliente"),
        "Director":f"{val.get("nombre_contacto")} {val.get("nombre_contacto")}",
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
  for val in cli.clientes:
    if(
     val.get("pais")== pais or
     (val.get("region")== region or val.get("region") == None) and
     (val.get("ciudad")== ciudad or val.get("ciudad") == None)
    ):
      clientZone.append(val)
  return  clientZone  

def getAllClientCiudad (ciudad):
  clienteCiud= list()
  for val in cli.clientes:
    if(
     (val.get("ciudad")== ciudad or val.get("ciudad") == None)
    ):
      clienteCiud.append(val)
  return  clienteCiud

def getAllClientDireccion1():
  clientDireccion1= list()
  for val in cli.clientes:
    direccion1= dict({ 
    "codigo_cliente": val.get("codigo_cliente"),
    "nombre_cliente": val.get("nombre_cliente"),
    "linea_direccion1": val.get("linea_direccion1")
    })
    clientDireccion1.append(direccion1)
  return clientDireccion1

def getAllClientTelefono():
  clientTelefono= list()
  for val in cli.clientes:
    telefono= dict({ 
    "codigo_cliente": val.get("codigo_cliente"),
    "nombre_cliente": val.get("nombre_cliente"),
    "telefono": val.get("telefono")
    })
    clientTelefono.append(telefono)
  return clientTelefono

def getAllClientCreditEntre():
  clientCredit= list()
  for val in cli.clientes:
   if(val.get("limite_credito")>= 5000 and val.get("limite_credito") <= 10000):
      clientCredit.append(val)
  return  clientCredit

def getAllClientFax():
  clientFax= list()
  for val in cli.clientes:
    fax= dict({
      "nombre_cliente": val.get("nombre_cliente"),
      "fax":  val.get("fax")
    })
    clientFax.append(fax)
  return clientFax

#filtro 6
def getAllClientsPais():
  paiscliente= []
  for val in cli.clientes:
    if (val.get("pais")==("Spain")):
      paiscliente.append(
        {
         "nombre": val.get("nombre_cliente"),
         "pais": val.get("pais")
        }
      )
  return paiscliente


def menu():
  print(""" 
Reportes de los clientes
1.Obtener todos los clientes (codigo y nombre)
2.Obtener un cliente por su codigo(codigo y su nombre)
3.Obtener toda la informacion de un cliente segun su limite de credito y ciudad
4.
""")
  opcion = int(input("\nSeleccione una de las opciones:"))
  if(opcion == 1):
    print(tabulate(getAllClientesName(),tablefmt="grid"))
  elif(opcion == 2):
    codigo= int(input("Ingrese el codigo del cliente: "))
    print(tabulate(getOneClientcodigo(codigo),tablefmt="grid"))
  elif(opcion == 3):
    clienteCredic= float(input)("/n Ingrese el limite de credito")


  






    
  
 


