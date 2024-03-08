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

#formas pagos_ filtro 14
def getAllAñoFormasPa():
    formaspago= []
    formasVistas= set()
    for val in pa.pago:
        forma_pago= ("forma_pago")
        if forma_pago not in ("formasVistas"):
            formaspago.append({ 
                "codigo_cliente":val.get("codigo_cliente"),
                "forma_pago":val.get("forma_pago"),
                "total":val.get("total")
            })
    formasVistas.add(forma_pago)
    
    return formaspago 
        
    
