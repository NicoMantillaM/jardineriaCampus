import storage.pedido as pe
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

