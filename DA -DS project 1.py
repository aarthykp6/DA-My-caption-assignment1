#Different Set Operations 

A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
print("Union :", A | B)
print("Intersection :", A & B)
print("Difference :", A - B)
print("Symmetric difference :", A ^ B)
#output
#Union : {0, 1, 2, 3, 4, 5, 6, 8}
#Intersection : {2, 4}
#Difference : {0, 8, 6}
#Symmetric difference : {0, 1, 3, 5, 6, 8}