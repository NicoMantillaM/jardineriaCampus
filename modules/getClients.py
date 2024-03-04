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
     val.get("pais")== pais and
     (val.get("region")== region or val.get("region") == None) or
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

def getAllDireccion1 ():
  clienteDirecio1= list()
  for val in cli.clientes:
    direcion1= dict({ 
    "codigo_cliente": val.get("codigo_cliente"),
    "nombre_cliente": val.get("nombre_cliente"),
    "linea_direccion1": val.get("linea_direccion1")
    })
    clienteDirecio1.append(direcion1)
  return clienteDirecio1


    
  
 


