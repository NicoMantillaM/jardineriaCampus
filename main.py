from tabulate import tabulate

import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPago as pago

import sys
#def menu():
#    contador = 1
#     print("Menu Principal")
#     for nombre, objeto in sys.modules.items():
#         if nombre.startswith("modules"):
#             modulo = getattr(objeto, "__name__", None)
#             if(modulo != "modules"):
#                 print(f"""{contador}. {modulo.split("get")[-1]} """)
#                 contador += 1
# menu()

if(__name__ == "__main__"):
   def menu():
    #https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
    print("""
Menu Principal
1.cliente
2.oficina 
3.empleado
4.pedido
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion==1):
        cliente.menu()
    elif(opcion==2):
        oficina.menu()
    elif(opcion==3):
        empleado.menu()
    elif(opcion==4):
        pedido.menu()
menu()
