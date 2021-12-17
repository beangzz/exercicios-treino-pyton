#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

ganhador = 0
jogadas = ("PEDRA","PAPEL","TESOURA")

pontos_jogador1 = 0
pontos_jogador2 = 0

print("Bem vindo")

while (ganhador == 0):
    jogador1 = input("Jogador 1, escolha sua jogada: ").upper()
    jogador2 = input("Jogador 2, escolha sua jogada: ").upper()


    if (jogador1 not in jogadas or jogador2 not in jogadas):
        print("Jogada inválida, tente novamente")
        continue
        
    else:
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


    if (ganhador == 1):
        print("O jogador 1 jogou {}, enquanto o jogador 2 jogou {}, o ganhador foi o Jogador 1".format(jogador1,jogador2))
        pontos_jogador1 += 1

    elif (ganhador == 2):
        print("O jogador 1 jogou {}, enquanto o jogador 2 jogou {}, o ganhador foi o Jogador 2".format(jogador1,jogador2))
        pontos_jogador2 += 1

    resposta = input("Deseja jogar novamente? ").upper()
    
    if (resposta == "SIM"):
        ganhador = 0
        continue
    elif (resposta == "NAO" or resposta == "NÃO"):
        break
    else:
        ganhador = 0

print("O jogador 1 fez {} pontos e o jogador 2 fez {} pontos".format(pontos_jogador1,pontos_jogador2))

