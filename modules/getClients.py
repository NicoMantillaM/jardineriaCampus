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

def getAllClientEmpleCodi():
  clientEmCod =list()
  for val in cli.clientes:
    codigoEmpDup= dict({
    "codigo_empleado_rep_ventas": val.get("codigo_empleado_rep_ventas")
    if codigo_empleado:
       if codigo_empleado in employee_codes:
          employee_codes[codigo_empleado] += 1
       else:
          employee_codes[codigo_empleado] = 1
    
    codigoEmpDup = [code for code, count in clientEmCod.items() if count > 1]  })
  return codigoEmpDup







    
  
 


