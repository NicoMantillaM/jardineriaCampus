import storage.pago as pa 

#pagos- filtro 13
def getAllAñoPaypal():
    pagosPaypal= []
    for val in pa.pago:
        if ("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"): 
            pagosPaypal.append({
                "codigo_cliente": val.get ("codigo_cliente"),
                "forma_pago": val.get ("forma_pago"),
                "fecha_pago": val.get ("fecha_pago"),
                "total": val.get ("total")
             })
    pagosPaypal= sorted(pagosPaypal, key=lambda x: x  ["total"], reverse=True )
    return pagosPaypal

