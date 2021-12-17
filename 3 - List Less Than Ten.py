#Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista_menor_5 = []
lista_maior_5 = []


for i in lista:
    if (i < 5):
        lista_menor_5.append(i)
    else:
        lista_maior_5.append(i)

print("Os números da lista menores que 5 são: ", lista_menor_5)
print("Os números da lista maiores que 5 são: ",lista_maior_5)

#~~~~~~~~
        
numero = int(input("Digite um número: "))
menor_que_num = []
maior_que_num = []

for i in lista:
    if (i < numero):
        menor_que_num.append(i)
    else:
        maior_que_num.append(i)

print("Os números da lista menores que {} são: {}".format(numero,menor_que_num))
print("Os números da lista maiores que {} são: {}".format(numero,maior_que_num))
