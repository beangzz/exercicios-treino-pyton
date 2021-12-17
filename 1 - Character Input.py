#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras:

#Ad on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


nome = input("Insira seu nome:")
idade = int(input("Insira sua idade:"))

ano_atual=2021

diferenca = 100-idade

ano_100 = ano_atual+diferenca

vezes = int(input("Quantas vezes você gostaria de imprimir?"))

# Dava pra fazer : ~~for i in range(1,vezes+1):~~
print(vezes * "{}, você completará 100 anos daqui a {} anos, no ano de {}!\n".format(nome,diferenca,ano_100))

