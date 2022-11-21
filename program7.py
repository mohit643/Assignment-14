 # Write a Python script to remove all non int values from a list.



list=[eval(x) for x in input("enetr a list supreted with commo..").split(',')]

for i in range(len(list)):
  
  
  if type(list[i])!=int:
    list[i]
    list[i].remove(list[i])
    
print(list)   