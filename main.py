import modules.getClients as cliente

from tabulate import tabulate
 
# assign data
mydata = [
    ["Nikhil", "Delhi"], 
    ["Ravi", "Kanpur"], 
    ["Manish", "Ahmedabad"], 
      ["Prince", "Bangalore"]
]
 
# create header
head = ["Name", "City"]
 
# display table
print (tabulate(cliente.getAllClientContd('France')))
