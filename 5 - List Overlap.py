#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random
a = []
b = []

tamanho1 = random.randint(1, 20)
tamanho2 = random.randint(1, 20)


while (len(a) < tamanho1):
    a.append(random.randint(0, 20))

while (len(b) < tamanho2):
    b.append(random.randint(0, 20))

a.sort()
b.sort()
print(a)
print(b)

lista = []

for i in a:
    if ((i in b) and (i not in lista)):
        lista.append (i)


lista.sort()

print (lista)