import storage.pedido as pe

from tabulate import tabulate

#filtro 7
def getAllEstadoPedido():
    estadoPedidos = []
    for val in pe.pedido:
        estadoPedidos.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "estado": val.get('estado')
                    })
    return estadoPedidos

#filtro 9
from datetime import datetime

# delvuelve un listado con el codgio d epedido,,
#codigo de cliente fecha espeada y
#fecha de entrega de los pedidos que no 
#han sido entregados a tiempo.

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado= []
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")    
        if val.get("estado") == "Entregado":
            date_1= "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2= "/".join(val.get("fecha_esperada").split("-")[::-1])
            star= datetime.strptime(date_1,"%d/%m/%Y" )
            end= datetime.strptime(date_2,"%d/%m/%Y")
            diff= end.date( ) - star.date()
            if(diff.days < 0):       
                pedidosEntregado.append({ 
                "codigo_pedido": val.get("codigo_pedido"),
                "codigo_cliente": val.get ("codigo_cliente"),
                "fecha_esperada": val.get("fecha_esperada"),
                "fecha_entrega": val.get("fecha_entrega")                                               
            })                        
    return pedidosEntregado


#filtro 10    
    
def getAllPedidosEntregadosDosDiasAnt():
    pedidosEntregadoAntes= []
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")    
        if val.get("estado") == "Entregado":
            date_1= "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2= "/".join(val.get("fecha_esperada").split("-")[::-1])
            star= datetime.strptime(date_1,"%d/%m/%Y" )
            end= datetime.strptime(date_2,"%d/%m/%Y")
            diff= end.date( ) - star.date()
            if(diff.days >=2 ):       
                pedidosEntregadoAntes.append({ 
                "codigo_pedido": val.get("codigo_pedido"),
                "codigo_cliente": val.get ("codigo_cliente"),
                "fecha_esperada": val.get("fecha_esperada"),
                "fecha_entrega": val.get("fecha_entrega")                                               
            })                        
    return pedidosEntregadoAntes

#filtro 11  

def getAllPedidosRechazados2009():
    pedidosRechazados= []
    for val in pe.pedido:
        if "2009" in val.get("fecha_pedido") and val.get("estado")== "Rechazado":        
            pedidosRechazados.append(val)                                                                   
    return pedidosRechazados


#filtro 12

def getAllEnEnero():
    pedidosEnero= []
    for val in pe.pedido:
        fecha_entrega = val.get ("fecha_entrega")
        if fecha_entrega:
            date_1= "/".join(val.get("fecha_entrega").split("-")[::-1])   
            start= datetime.strptime(date_1,"%d/%m/%Y")    
            if start.month == 1 and val.get("estado")=="Entregado":
                pedidosEnero.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                    "estado_pedido": val.get("estado")
                })                                                         
    return pedidosEnero

def menu():
    print(""" 
1.Obtener los distintos estados por los que puede pasar un pedido 
2.Obtener codigo-pedido,  codigo-cliente, fecha-esperada y fecha-entrega de los pedidos entregados a tiempo
3.Obtener informacion de los pedidos cuya entrega ha sido al menos dos días antes de la fecha esperada
4.Obtener todos los pedidos que fueron rechazados en el 2009, con su respectivo comentario
5.Obtener todos los pedidos que fueron entregados en el mes de enero de cualquier año
""")
    opcion = int(input("\nSeleccione una de las opciones:"))
    if(opcion == 1):
        print(tabulate(getAllEstadoPedido(),tablefmt="grid"))
    elif(opcion == 2):
        print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(),tablefmt="grid"))
    elif(opcion == 3):
        print(tabulate(getAllPedidosEntregadosDosDiasAnt(),tablefmt="grid"))
    elif(opcion == 4):
        print(tabulate(getAllPedidosRechazados2009(),tablefmt="grid"))
    elif(opcion == 5):
        print(tabulate(getAllEnEnero(),tablefmt="grid"))