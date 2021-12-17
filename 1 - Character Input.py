#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. Print out that many copies of the previous message.

nome = input("Insira seu nome:")
idade = int(input("Insira sua idade:"))

ano_atual = 2021

diferenca = 100 - idade

ano_100 = ano_atual + diferenca

vezes = int(input("Quantas vezes você gostaria de imprimir?"))

print(vezes * "{}, você completará 100 anos daqui a {} anos, no ano de {}!\n".format(nome,diferenca,ano_100))
