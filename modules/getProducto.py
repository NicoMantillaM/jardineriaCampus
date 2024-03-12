import storage.producto as pr
from tabulate import tabulate

#Devuelve un listado con todas los productos q pertenecen a la gama ornamentales
#y q tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta, mayor a menor

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in pr.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):    
        condiciones[i] = {
        "codigo": val.get("codigo_producto"), 
        "venta": val.get("precio_venta"),
        "nombre": val.get("nombre_producto"),   
        "gama": val.get("gama"), 
        "dimensiones": val.get("dimensiones"),
        "proveedor": val.get("proveedor"),              
        "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
        "stock": val.get("cantidad_stock"),
        "base": val.get("precio_proveedor")
        }
                
    return condiciones

def menu():
    while True:
        print("""
REPORTES DE LOS PRODUCTOS
0.Regresar al menu principal
1.Obtener productos de una categoria ordenando su precio de venta y rectificando que su cantidad de stock sea superior
""")
        opcion=int(input("Seleccione una de las opciones: "))
        if (opcion==1):
            gama=input("Ingrese la gama del producto: ")
            stock=int(input("Ingrese el stock del producto: "))
            print(tabulate(getAllStocksPriceGama(gama,stock),headers="keys",tablefmt="grid"))
        elif(opcion==0):
            break
