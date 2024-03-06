import storage.empleado as em 

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail= []
    for val in em.empleado:
       if (val.get("codigo_jefe") == codigo):
           nombreApellidoEmail.append(
               {
                   "nombre": val.get("nombre"),
                   "apellidos": f'{val.get ("apellido1")}{val.get("apellido2)")}',
                   "email": val.get("email"),
                   "jefe": val.get("codigo_jefe")
               }

           )
    return nombreApellidoEmail 

#filtro 4
def getAllNomApeJefeEmpresa():
    nombreApellidoEmailJefeEmpresa = []
    
    for val in em.empleado:
        if (val.get ("codigo_jefe") == None ): 
            nombreApellidoEmailJefeEmpresa.append({

                'nombre': val.get('nombre'),
                'apellidos': f'{val.get("apellido1")} {val.get("apellido2")}',
                'email': val.get('email'),
                'puesto': val.get ('puesto'),
                'jefe': val.get('codigo_jefe'),
            }
            )
    return nombreApellidoEmailJefeEmpresa


#filtro 5
def getAllNomApePuestoVec():
    nombreApellidoPuesto=[]
    for val in em.empleado:
         if (val.get("puesto") != ("Representante Ventas")):
              nombreApellidoPuesto.append(
               {
                   "nombre": val.get("nombre"),
                   "apellidos": f'{val.get ("apellido1")}{val.get("apellido2)")}',
                   "puesto": val.get("puesto")
               }

           )
    return nombreApellidoPuesto



             
             