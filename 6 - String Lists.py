#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

palavra = input("Escreva: ").strip()
palavra2 = []


palavra = palavra.upper()


for i in palavra:
    palavra2.append(i)

palavra2.reverse()

index = 0
valor = False


for i in palavra:
    if (i == palavra2[index]):
        valor = True
    else:
        valor = False
    index = index+1

if (valor == True):
    print("{} é um palíndromo".format(palavra))
else:
    print("{} não é um palíndromo".format(palavra))