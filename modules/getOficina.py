import os
import requests
from tabulate import tabulate

def getAllDataOficina():
  #json-server storage/oficina.json -b 5509
  peticion=requests.get("http://192.168.1.11:5509")
  data= peticion.json()
  return data
    


def getAllCodigoCiudad():
    codigoCiudad= []
    for val in getAllDataOficina:
        codigoCiudad.append({
           "codigo":val.get("codigo_oficina"),
           "ciudad":val.get ("ciudad")
        })
    return codigoCiudad

#devuelveme un listado con la ciudad y el telefono 
#de las oficinas de españa

def getAllCiudadTelefono(pais):
    ciudadTelefono= []
    for val in getAllDataOficina:
        if (val.get("pais")==pais):
           ciudadTelefono.append({
           "ciudad":val.get("ciudad"),
           "telefono":val.get ("telefono"),
           "oficinas":val.get("codigo_oficina"),
           "pais":val.get("pais")
         })
    return ciudadTelefono

def getOneCodigoPostal(codigoPost):
    for val in getAllDataOficina:
        if (val.get("codigo_postal")==codigoPost):
            return [{
            "codigo_oficina": val.get("codigo_oficina"),
            "region": val.get("region"),
            "telefono":val.get('telefono')
          }]

def menu():
    while True:
        print(""" 
Reportes de las oficinas
0.Regresar a menu principal
1.Obtener todos los codigos de oficina con su ciudad 
2.Obtener la ciudad y telefono de oficina segun el pais
3.Obtener el codigo de oficina, la region y el telefono de la oficina por codigo postal
  -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL            
""")
        try:
            opcion = int(input("\nSeleccione una de las opciones:"))
            if(opcion == 1):
                print(tabulate(getAllCodigoCiudad(),tablefmt="grid"))
            elif(opcion == 2):
                pais= str(input("\nIngrese el pais: " ))
                print(tabulate(getAllCiudadTelefono(pais),tablefmt="grid"))
            elif(opcion == 3):
                codigoPost= str(input("\nIngrese el codigo postal: " ))
                print(tabulate(getOneCodigoPostal(codigoPost),tablefmt="grid"))
            elif(opcion == 0):
                    break
        except KeyboardInterrupt:
            break