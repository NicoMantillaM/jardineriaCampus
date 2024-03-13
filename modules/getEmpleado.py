import storage.empleado as em 

from tabulate import tabulate

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

def menu():
    while True:
        
        print("""
Reportes de los empleados             
0.Regresar a menu principal
1.Obtener la informacion del jefe por su codigo
2.Obtener el nombre, apellidos y email del jefe de la empresa
3.Obtener el nombre, apellidos y puesto de aquellos empleados que no sean Representantes de ventas
    -PRESIONA CTRL + C PARA REGRESAR AL MENU PRINCIPAL
""")
        try:
            opcion = int(input("\nSeleccione una de las opciones:"))
            if(opcion == 1):
                codigo=int(input("\nIngrese el codigo de jefe: " ))
                print(tabulate(getAllNombreApellidoEmailJefe(codigo),tablefmt="grid"))
            elif(opcion == 2):
                print(tabulate(getAllNomApeJefeEmpresa(),tablefmt="grid"))
            elif(opcion == 3):
                print(tabulate(getAllNomApePuestoVec(),tablefmt="grid"))
            elif(opcion == 0):
                break
        except KeyboardInterrupt:
            print()
            print()
            print("saliendo...")
            break
