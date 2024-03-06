import storage.pedido as ped

def getAllProcesoPedido():
    ProcesoPedidos = []
    for val in ped.pedido:
        ProcesoPedidos.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "estado": val.get('estado')
                    })
    return ProcesoPedidos