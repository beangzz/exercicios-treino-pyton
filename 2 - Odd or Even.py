#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


numero_escolhido = int(input("Escolha um número: "))

if (numero_escolhido % 2 == 0):
    print("Seu número é par")
    if (numero_escolhido % 4 ==0):
        print("Seu número também é dividisível por 4!")

else:
    print("Seu número é impar")

numero_1 = int(input("Escolha um novo número: "))
numero_2 = int(input("Escolha um outro número: "))

if (numero_1 % numero_2 == 0):
    print("{} é divisísel por {}".format(numero_1,numero_2))
else:
    print("{} não é divisísel por {}".format(numero_1,numero_2))