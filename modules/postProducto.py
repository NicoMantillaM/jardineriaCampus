import os
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG
import modules.getProducto as gPro
import re 


def postProducto():
    #json-server storage/producto.json -b 5505
    producto = dict()
    while True:
        try:
            if not producto.get("codigo_producto"):
                codigo = input("Ingrese el codigo del producto (Eje:11): ")
                if re.match(r'^[A-Z]{2}-\d{1,3}$', codigo) is not None:
                    data= gPro.getProductoCodigo(codigo)
                    if(data):
                        print(tabulate(data,tablefmt="Fancy_grid"))
                        raise Exception("El codigo del producto ya existe")
                    else:
                        producto["codigo_producto"]=codigo
                else:
                    raise Exception("El codigo no cumple con el estandar, intentelo denuevo")
                
            if not producto.get("nombre"):
                nombre=input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Za-záéíóúüñ\s\d.,:;()-]+$',nombre)is not None):
                    producto["nombre"]=nombre
                else:
                    raise Exception("El nombre del producto no cumple con el estandar, intentelo denuevo")
                
            if not producto.get("gama"):
                gama= input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
            if re.match(r'^[0-4]$', gama) is not None:  
                gama = int(gama)
                data = gG.getAllNombre()[gama]
                producto["gama"] = gama
            else:
                raise Exception("La gama del producto no cumple con el estandar, intentelo denuevo")
            
            if(not producto.get("dimensiones")):
                dimensiones=input("Ingrese las dimensiones del producto: ")
                if(re.match(r'^\d{1,3}\s*-\s*\d{1,3}$',dimensiones)is not None):
                     producto["dimensiones"]=dimensiones
                else:
                    raise Exception("Las dimensiones del producto no cumplen con el estandar, intentelo denuevo")
                
            if(not producto.get("proveedor")):
                proveedor=input("Ingrese el proovedor del producto: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',proveedor)is not None):
                    producto["proveedor"]=proveedor
                else:
                    raise Exception("El proveedor del producto no cumple con el estandar, intentelo denuevo")
                
            if(not producto.get("descripcion")):
                descripcion=input("Ingrese la descripcion del producto: ")
                if(re.match(r'^[^\n]+$',descripcion)is not None):
                    producto["descripcion"]=descripcion
                else:
                    raise Exception("La descripcion del producto no cumple con el estandar, intentelo denuevo")  
                
            if(not producto.get("cantidad_en_stock")):
                cantidad_en_stock=input("Ingrese la cantidad en stock del producto: ")
                if(re.match(r'^[0-9]{2,3}$',cantidad_en_stock)is not None):
                    cantidad_en_stock= int(cantidad_en_stock)
                    producto["cantidad_en_stock"]=cantidad_en_stock
                else:
                    raise Exception("La cantidad en stock no cumple con el estandar, intentelo denuevo") 
                
            if(not producto.get("precio_venta")):
                precio_venta=input("Ingrese el precio de venta del producto: ")
                if(re.match(r'^[0-9]{1,3}$',precio_venta)is not None):
                    precio_venta= int(precio_venta)
                    producto["precio_venta"]=precio_venta
                else:
                    raise Exception("El precio de venta del producto no cumple con el estandar, intentelo denuevo")  

            if(not producto.get("precio_proveedor")):
                precio_proveedor=input("Ingrese el precio de venta del producto: ")
                if(re.match(r'^[0-9]{1,3}$',precio_proveedor)is not None):
                    precio_proveedor= int(precio_proveedor)
                    producto["precio_proveedor"]=precio_proveedor
                    break
                else:
                    raise Exception("El precio de venta del producto no cumple con el estandar, intentelo denuevo")     
                
        except Exception as error:
            print(error)

    peticion = requests.post("http://154.38.171.54:5008/productos", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def deleteProduct(id):
    data= gPro.getProductoCodg(id)
    if(len(data)):

        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "message": "producto no encontrado",
                    "id": id
            }],
            "status": 400,
        }

def updateProducto(id):
    data= gPro.getProductoCodg(id)
    if(len(data)):
        producto = dict()
        while True:
            try: 
                if not producto.get("codigo_producto"):
                    codigo = input("Ingrese el codigo del producto (Eje:11679): ")
                    if re.match(r'^[A-Z]{2}-\d{1,3}$', codigo) is not None:
                        data= gPro.getProductoCodigo2(codigo)
                        if(data):
                            print(tabulate(data,tablefmt="Fancy_grid"))
                        else:
                            producto["codigo_producto"]=codigo
                    else:
                        raise Exception("El codigo no cumple con el estandar, intentelo denuevo")
                    
                if not producto.get("nombre"):
                    nombre=input("Ingrese el nombre del producto: ")
                    if(re.match(r'^[A-Za-záéíóúüñ\s\d.,:;()-]+$',nombre)is not None):
                        producto["nombre"]=nombre
                    else:
                        raise Exception("El nombre del producto no cumple con el estandar, intentelo denuevo")
                    
                if not producto.get("gama"):
                    gama= input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
                if re.match(r'^[0-4]$', gama) is not None:  
                    gaman = int(gama)
                    gama = gG.getAllNombre()[gaman]
                    producto["gama"] = gama
                else:
                    raise Exception("La gama del producto no cumple con el estandar, intentelo denuevo")
                
                if(not producto.get("dimensiones")):
                    dimensiones=input("Ingrese las dimensiones del producto: ")
                    if(re.match(r'^\d{1,3}\s*-\s*\d{1,3}$',dimensiones)is not None):
                        producto["dimensiones"]=dimensiones
                    else:
                        raise Exception("Las dimensiones del producto no cumplen con el estandar, intentelo denuevo")
                    
                if(not producto.get("proveedor")):
                    proveedor=input("Ingrese el proovedor del producto: ")
                    if(re.match(r'^([A-Za-z][a-z]*\s*)+$',proveedor)is not None):
                        producto["proveedor"]=proveedor
                    else:
                        raise Exception("El proveedor del producto no cumple con el estandar, intentelo denuevo")
                    
                if(not producto.get("descripcion")):
                    descripcion=input("Ingrese la descripcion del producto: ")
                    if(re.match(r'^[^\n]+$',descripcion)is not None):
                        producto["descripcion"]=descripcion
                    else:
                        raise Exception("La descripcion del producto no cumple con el estandar, intentelo denuevo")  
                    
                if(not producto.get("cantidad_en_stock")):
                    cantidad_en_stock=input("Ingrese la cantidad en stock del producto: ")
                    if(re.match(r'^[0-9]{2,3}$',cantidad_en_stock)is not None):
                        cantidad_en_stock= int(cantidad_en_stock)
                        producto["cantidad_en_stock"]=cantidad_en_stock
                    else:
                        raise Exception("La cantidad en stock no cumple con el estandar, intentelo denuevo") 
                    
                if(not producto.get("precio_venta")):
                    precio_venta=input("Ingrese el precio de venta del producto: ")
                    if(re.match(r'^[0-9]{1,3}$',precio_venta)is not None):
                        precio_venta= int(precio_venta)
                        producto["precio_venta"]=precio_venta
                    else:
                        raise Exception("El precio de venta del producto no cumple con el estandar, intentelo denuevo")  

                if(not producto.get("precio_proveedor")):
                    precio_proveedor=input("Ingrese el precio de venta del producto: ")
                    if(re.match(r'^[0-9]{1,3}$',precio_proveedor)is not None):
                        precio_proveedor= int(precio_proveedor)
                        producto["precio_proveedor"]=precio_proveedor
                        break
                    else:
                        raise Exception("El precio del proveedor del producto no cumple con el estandar, intentelo denuevo")     
                    
            except Exception as error:
                print(error)

        peticion = requests.put(f"http://154.38.171.54:5008/productos/{id}", data=json.dumps(producto))
        res = peticion.json()
        res["Mensaje"]= "Producto Guardado"
        return [res]
    else:
        return[{
            "message": "Producto no encontrado",
            "id": id
        }] 

# def updateProductoCodigo(iD):
#     while True:
#         # if opcion == 1:
#         #     actuzali = input("ingrese el id a actualizar")
#         #     if re.match(r"^[0-9]+$)", actuzali):
#         #         actuzali = int(actuzali)
#         if(iD != None):
#             producto = gPro.getProductoCodg(iD)
#             if (producto):
#                 print(tabulate(producto, headers="keys", tablefmt="grid"))
#                 opcion = int(input("""
#                             ¿Este el producto que desea actualizar?
#                                         1. Si
#                                         2. No
#                 """))
#                 if (opcion):
#                     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#                     producto[0]["codigo_producto"] = input("Ingrese el nuevo codigo del producto: ")
#                     peticion = requests.put(f"http://154.38.171.54:5008/productos/{producto[0].get("id")}", headers=headers , data=json.dumps(producto, indent=4))
#                     data = peticion.json()
#                     return [data[0]]
#                 else:
#                     iD = None
#             else:
#                 print(f"El producto {iD} no existe ")
#                 iD = None
#         else:
#             iD = input("Ingrese el codigo del producto que desea actualizar: ") 

       


def menu():
    while True:
        os.system("clear")
        print ("""
ADMINISTRAR DATOS DE PRODUCTOS
0.Regresar al menu principal
1.Guardar un producto nuevo
2.Eliminar un producto
3.Actualizar producto
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = input("\nSelecione una de las opciones: ")
            if(re.match(r'^[0-3]$', opcion)is not None):
                opcion=int(opcion)
            if(opcion == 1):
                print(tabulate(postProducto(), tablefmt="Fancy_grid"))
                input("Precione una tecla para continuar.....")
            if(opcion == 2):
                idProducto = int(input("Ingrese el id del producto que desea eliminar: "))
                print(tabulate(deleteProduct(idProducto)["body"], tablefmt="Fancy_grid"))
                input("Presione una tecla para continuar......")
            if(opcion == 3):
                idProducto = int(input("Ingrese el id del producto que desea Actualizar : "))
                print(tabulate(updateProducto(idProducto), tablefmt="Fancy_grid"))
                input("Presione una tecla para continuar......")

            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break


#    while True: 
#         while True:
#             os.system ("clear")
#             print("""
                
#                 ELIJA EL DATO QUE DESEA ACTUALIZAR:
                  
#                 1. Codigo_producto
#                 2. Nombre
#                 3. Gama
#                 4. Dimensiones
#                 5. Proveedor
#                 6. Descripcion
#                 7. Cantidad_en_stock
#                 8. Precio_venta
#                 9. Precio_proveedor
#                   -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
#                 #    input("Precione una tecla para continuar.....")
#                 """)
#             opcion = int(input("Ingrese la opcion a actualizar: "))
#             if(re.match(r'[0-9]+$', opcion)is not None):
#                 opcion = int(opcion)
#                 if(opcion>=0 and opcion<=9):