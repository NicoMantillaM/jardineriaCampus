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
                codigo = input("Ingrese el codigo del producto (Eje:11679): ")
                if re.match(r'^[0-9]+$', codigo) is not None:
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
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre)is not None):
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
                if(re.match(r'^[0-9]{2,3}-[0-9]{2,3}$',dimensiones)is not None):
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
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',descripcion)is not None):
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
                if(re.match(r'^[0-9]{2,3}$',precio_venta)is not None):
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

    peticion = requests.post("http://192.168.1.11:5505", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"]= "Producto Guardado"
    return [res]

def deleteProduct(id):
    data = gPro.getProductoCodigo(id)
    if(len(data)):

        peticion = requests.delete(f"http://192.168.1.11:5505/productos/{id}")
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
    data=gPro.getProductCodigo(id)
    if(len(data)):
            producto=dict()
            while True:
                try:
                    if(not producto.get("codigo_producto")):
                        codigo=input("Ingrese el codigo del producto: ")
                        if(re.match(r'^[A-Z]{2}-[0-9]{2,3}$',codigo)is not None):
                            data=(gPro.getProductCodigo2(codigo))
                            if(data):
                                print(tabulate(data,headers="keys", tablefmt="grid"))
                                raise Exception("El producto ya existe")
                            else:
                                producto["codigo_producto"]=codigo
                        else:
                            raise Exception("El codigo del producto no cumple con el estandar establecido")
                        
                    if(not producto.get("nombre")):
                        nombre=input("Ingrese el nombre del producto: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre)is not None):
                            producto["nombre"]=nombre
                        else:
                            raise Exception("El nombre del producto no cumple con el estandar establecido")
                        
                    if not producto.get("gama"):
                        gama= input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
                    if re.match(r'^[0-4]$', gama) is not None:  
                        gamab = int(gama)
                        gama = gG.getAllNombre()[gamab]
                        producto["gama"] = gama
                    else:
                        raise Exception("La gama del producto no cumple con el estándar establecido")
                    
                    if(not producto.get("dimensiones")):
                        dimensiones=input("Ingrese las dimensiones del producto: ")
                        if(re.match(r'^[0-9]{2,3}-[0-9]{2,3}$',dimensiones)is not None):
                            producto["dimensiones"]=dimensiones
                        else:
                            raise Exception("Las dimensiones del producto no cumplen con el estandar establecido")
                        
                    if(not producto.get("proveedor")):
                        proveedor=input("Ingrese el proovedor del producto: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',proveedor)is not None):
                            producto["proveedor"]=proveedor
                        else:
                            raise Exception("El proveedor del producto no cumple con el estandar establecido")
                        
                    if(not producto.get("descripcion")):
                        descripcion=input("Ingrese la descripcion del producto: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',descripcion)is not None):
                            producto["descripcion"]=descripcion
                        else:
                            raise Exception("La descripcion del producto no cumple con el estandar establecido")  
                        
                    if(not producto.get("cantidad_en_stock")):
                        cantidad_en_stock=input("Ingrese la cantidad en stock del producto: ")
                        if(re.match(r'^[0-9]{2,3}$',cantidad_en_stock)is not None):
                            cantidad_en_stock= int(cantidad_en_stock)
                            producto["cantidad_en_stock"]=cantidad_en_stock
                        else:
                            raise Exception("La cantidad en stock no cumple con el estandar establecido") 
                        
                    if(not producto.get("precio_venta")):
                        precio_venta=input("Ingrese el precio de venta del producto: ")
                        if(re.match(r'^[0-9]{2,3}$',precio_venta)is not None):
                            precio_venta= int(precio_venta)
                            producto["precio_venta"]=precio_venta
                        else:
                            raise Exception("El precio de venta del producto no cumple con el estandar establecido")  

                    if(not producto.get("precio_proveedor")):
                        precio_proveedor=input("Ingrese el precio de venta del producto: ")
                        if(re.match(r'^[0-9]{1,3}$',precio_proveedor)is not None):
                            precio_proveedor= int(precio_proveedor)
                            producto["precio_proveedor"]=precio_proveedor
                            break
                        else:
                            raise Exception("El precio de venta del producto no cumple con el estandar establecido")                    
                except Exception as error:
                    print(error)
                    pet=requests.put(f"http://172.16.103.37:5503/producto/{id}", data=json.dumps(producto))
                    res=pet.json()
                    res["Mensaje"] = "Producto Guardado"
                    return [res]
    else:
        return{
            "Body":[{
                "Mensaje":"El producto no ha sido encontrado",
                "ID":id
            }],
                "Status":400
            }   

def menu():
    while True:
        os.system("clear")
        print ("""
ADMINISTRAR DATOS DE PRODUCTOS
0.Regresar al menu principal
1.Guardar un producto nuevo
2.Eliminar un producto
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(postProducto(), tablefmt="Fancy_grid"))
                input("Precione una tecla para continuar.....")
            if(opcion == 2):
                idProducto = input("Ingrese el id del producto que desea eliminar: ")
                print(tabulate(deleteProduct(idProducto)["body"], tablefmt="Fancy_grid"))
                input("Presione una tecla para continuar......")

            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            break

