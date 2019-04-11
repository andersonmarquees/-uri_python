n = int(input())

while n > 0:

    player1 = str(input()).lower()
    player2 = str(input()).lower()

    if player1 == 'ataque' and player2 == 'pedra':
        print("Jogador 1 venceu")
    elif player2 == 'ataque' and player1 == 'pedra':
        print("Jogador 2 venceu")

    elif player1 == 'pedra' and player2 == 'papel':
        print("Jogador 1 venceu")
    elif player2 == 'pedra' and player1 == 'papel':
        print("Jogador 2 venceu")

    elif player1 == 'ataque' and player2 == 'papel':
        print("Jogador 1 venceu")
    elif player2 == 'ataque' and player1 == 'papel':
        print("Jogador 2 venceu")

    elif player1 == 'papel' and player2 == 'papel':
        print("Ambos venceram")

    elif player1 == 'pedra' and player2 == 'pedra':
        print("Sem ganhador")
    elif player1 == 'ataque' and player2 == 'ataque':
        print("Aniquilacao mutua")

    n -= 1





