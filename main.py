from tabulate import tabulate
import re
import os
import modules.getClients as cliente #Repcliente
import modules.postClients as pstcliente
import modules.getOficina as oficina
import modules.postOficina as pstoficina
import modules.getEmpleado as empleado #Repempleado
import modules.postEmpleado as pstempleado
import modules.getPedido as pedido
import modules.postPedido as pstpedido
import modules.getPago as pago
import modules.postPago as pstpago
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto


# import sys
# #def menu():
# #    contador = 1
# #     print("Menu Principal")1
# #     for nombre, objeto in sys.modules.items():
# #         if nombre.startswith("modules"):
# #             modulo = getattr(objeto, "__name__", None)
# #             if(modulo != "modules"):
# #                 print(f"""{contador}. {modulo.split("get")[-1]} """)
# #                 contador += 1
# # menu()

def menuCliente():
    while True:
        os.system ("clear")
        print("""
BIENVENIDO AL MENU DE CLIENTES              
0.Regresar al menu principal
1.Reportes de los clientes
2.Guardar, Actualizar y Eliminar clientes
""")
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            cliente.menu()
        if(opcion == 2):
            pstcliente.menu()
        elif(opcion == 0):
            break    



def menuEmpleado():
    while True:
        os.system ("clear")
        print("""
BIENVENIDO AL MENU DE EMPLEADOS              
0.Regresar al menu principal
1.Reportes de los empleados
2.Guardar, Actualizar y Eliminar empleados
""")
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            empleado.menu()
        if(opcion == 2):
            pstempleado.menu()
        elif(opcion == 0):
            break    


def menuOficina():
    while True:
        os.system ("clear")
        print("""
BIENVENIDO AL MENU DE OFICINA              
0.Regresar al menu principal
1.Reportes de la oficina
2.Guardar, Actualizar y Eliminar oficinas
""")
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            oficina.menu()
        if(opcion == 2):
            pstoficina.menu()
        elif(opcion == 0):
            break    

def menuPago():
    while True:
        os.system ("clear")
        print("""
BIENVENIDO AL MENU DE PAGOS              
0.Regresar al menu principal
1.Reportes de pagos
2.Guardar, Actualizar y Eliminar pagos
""")
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            pago.menu()
        if(opcion == 2):
            pstpago.menu()
        elif(opcion == 0):
            break       

def menuPedido():
    while True:
        os.system ("clear")
        print("""
BIENVENIDO AL MENU DE PEDIDOS              
0.Regresar al menu principal
1.Reportes de pedidos
2.Guardar, Actualizar y Eliminar pedidos
""")
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            pedido.menu()
        if(opcion == 2):
            pstpedido.menu()
        elif(opcion == 0):
            break       



def menuProducto():
    while True:
        os.system ("clear")
        print("""
BIENVENIDO AL MENU DE PRODUCTOS
0.Regresar al menu principal
1.Reportes de los productos
2.Guardar, Actualizar y Eliminar productos
""")
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            Repproducto.menu()
        if(opcion == 2):
            CRUDproducto.menu()
        elif(opcion == 0):
            break    




if(__name__ == "__main__"):
    while True:
        os.system("clear")
        print("""
Menu Principal
0.Salir
1.cliente
2.oficina 
3.empleado
4.pedido
5.pago
6.producto
""")
        
        opcion = int(input("\nSeleccione una de las opciones: "))
                        # if(re.match(r'[0-9]+$', opcion)is not None):
                        #     opcion = int(opcion)
                        #     if(opcion>=0 and opcion<=5):
        if(opcion==1):
            menuCliente()
        elif(opcion==2):
            menuOficina()
        elif(opcion==3):
            menuEmpleado()
        elif(opcion==4):
            menuPedido()
        elif(opcion==5):
            menuPago()
        elif(opcion==6):
            menuProducto()
        elif(opcion==0):
            break
       

