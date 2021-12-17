#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

ganhador = 0

print("Bem vindo")

while (ganhador == 0):
    jogada1 = input("Jogador 1, escolha sua jogada: ")
    jogada2 = input ("Jogador 2, escolha sua jogada: ")

    jogador1 = jogada1.upper()
    jogador2 = jogada2.upper()

    if (jogador1 == jogador2):
        print("Empate!")
        continue
    elif (jogador1 == "PEDRA"):
        if (jogador2 == "TESOURA"):
            ganhador = 1
        else:
            ganhador = 2
    elif (jogador1 == "TESOURA"):
        if (jogador2 == "PAPEL"):
            ganhador = 1
        else:
            ganhador = 2
    elif (jogador1 == "PAPEL"):
        if (jogador2 == "PEDRA"):
            ganhador = 1
        else:
            ganhador = 2
    else:
        print("Jogada inválida, tente novamente")
        continue
    if (ganhador == 1):
        print("O jogador 1 mandou {}, enquanto o jogador 2 jogou {}, o ganhador foi o Jogaor 1".format(jogada1,jogada2))
    elif (ganhador == 2):
        print("O jogador 1 mandou {}, enquanto o jogador 2 jogou {}, o ganhador foi o Jogaor 2".format(jogada1,jogada2))

    resposta = input("Deseja jogar novamente? ").upper()
    if (resposta == "SIM"):
        ganhador = 0
        continue
    else:
        break


