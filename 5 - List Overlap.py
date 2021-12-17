#Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:
#Randomly generate two lists to test this


import random

a = []
b = []

while (len(a) < random.randint(1, 20)):
    a.append(random.randint(0, 20))

while (len(b) < random.randint(1, 20)):
    b.append(random.randint(0, 20))

a.sort()
b.sort()

lista = []

for elemento in a:
    if ((elemento in b) and (elemento not in lista)):
        lista.append (elemento)

if (lista == []):
    print("As listas não possuem elemenos em comum")
else:
    print("Elementos em comum: ", lista)
