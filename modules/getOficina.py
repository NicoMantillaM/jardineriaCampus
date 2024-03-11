import storage.oficina as of 

from tabulate import tabulate


def getAllCodigoCiudad():
    codigoCiudad= []
    for val in of.oficina:
        codigoCiudad.append({
           "codigo":val.get("codigo_oficina"),
           "ciudad":val.get ("ciudad")
        })
    return codigoCiudad

#devuelveme un listado con la ciudad y el telefono 
#de las oficinas de españa

def getAllCiudadTelefono(pais):
    ciudadTelefono= []
    for val in of.oficina:
        if (val.get("pais")==pais):
           ciudadTelefono.append({
           "ciudad":val.get("ciudad"),
           "telefono":val.get ("telefono"),
           "oficinas":val.get("codigo_oficina"),
           "pais":val.get("pais")
         })
    return ciudadTelefono

def getOneCodigoPostal(codigoPost):
    for val in of.oficina:
        if (val.get("codigo_postal")==codigoPost):
            return [{
            "codigo_oficina": val.get("codigo_oficina"),
            "region": val.get("region"),
            "telefono":val.get('telefono')
          }]

def menu():
    print(""" 
1.Obtener todos los codigos de oficina con su ciudad 
2.Obtener la ciudad y telefono de oficina segun el pais
3.Obtener el codigo de oficina, la region y el telefono de la oficina por codigo postal
""")
    opcion = int(input("\nSeleccione una de las opciones:"))
    if(opcion == 1):
        print(tabulate(getAllCodigoCiudad(),tablefmt="grid"))
    elif(opcion == 2):
        pais= str(input("\nIngrese el pais: " ))
        print(tabulate(getAllCiudadTelefono(pais),tablefmt="grid"))
    elif(opcion == 3):
        codigoPost= str(input("\nIngrese el codigo postal: " ))
        print(tabulate(getOneCodigoPostal(codigoPost),tablefmt="grid"))
