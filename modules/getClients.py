import storage.cliente as cli

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
      return { 
      "codigo_cliente": val.get("codigo_cliente"),
      "nombre_cliente": val.get("nombre_cliente")
     }

def getAllClientCreditCiudad(limite_credit, ciudad):
  clienteCredic= list()
  for val in cli.clientes:
   if (val.get("limite_credito") >= limite_credit and val.get("ciudad") == ciudad):
      clienteCredic.append(val)
  return  clienteCredic

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


#def getAllClientContd(pais):
#  try:
#        from tabulate import tabulate
# except ModuleNotFoundError:
#        tabulate = None

#  clientPaisRe= list()
#  contador = 0
#  for val in cli.clientes:
#    if val.get('pais') == pais:
#        contador = contador + 1
#    clientPaisRe.append(contador)
# return clientPaisRe








    
  
 


