#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

numero_sorteado = random.randint(1, 9)
tentativas = 0
numero_usuario = 0

while (numero_usuario != numero_sorteado):
    usuario = input("Escreva sua tentativa: ")

    if (usuario == "sair" or usuario=="SAIR"):
        print("Que pena, o número secreto era {}!\nVocê usou {} tentativas".format(numero_sorteado, tentativas))
        break

    else:
        numero_usuario = int(usuario)
        if (numero_usuario < numero_sorteado):
            print("Seu chute foi menor do que o valor sorteado!")
        elif(numero_usuario> numero_sorteado):
            print("Seu chute foi maior do que o valor sorteado!")
        else:
            print("Você acertou! \nVocê usou {} tentativas".format(tentativas))
            break

    tentativas += 1

