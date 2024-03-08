from tabulate import tabulate

import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPago as pago


print (tabulate(pago.getAllAñoPaypal(),tablefmt="grid"))

