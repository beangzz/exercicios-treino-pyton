#and write a program that prints out all the elements of the list that are less than 5.
# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista_menor_5 = []
lista_maior_5 = []


for i in lista:
    if (i < 5):
        lista_menor_5.append(i)
    else:
        lista_maior_5.append(i)


numero = int(input("digite um número "))
menor_que_num = []
maior_que_num=[]
for i in lista:
    if (i < numero):
        menor_que_num.append(i)
    else:
        maior_que_num.append(i)

print(menor_que_num)
print(maior_que_num)
