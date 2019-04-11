entrada = list(map(int, input().split()))
p, j1, j2, r, a = entrada[0], entrada[1], entrada[2], entrada[3], entrada[4]

soma = j1 + j2

if p == 1 and soma % 2 == 1 and r == 0 and a == 0: # jogador1 escolheu par
    print("Jogador 2 ganha!")
elif p == 1 and soma % 2 == 0 and r == 0 and a == 0:
    print("Jogador 1 ganha!")
elif p == 1 and soma % 2 == 1 and r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif p == 1 and soma % 2 == 1 and r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif p == 1 and soma % 2 == 0 and r == 0 and a == 1:
    print("Jogador 1 ganha!")
elif p == 1 and soma % 2 == 0 and r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif p == 1 and soma % 2 == 0 and r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif p == 1 and soma % 2 == 1 and r == 0 and a == 1:
    print("Jogador 1 ganha!")


elif p == 0 and soma % 2 == 0 and r == 0 and a == 0: # jogador1 escolheu impar
    print("Jogador 2 ganha!")
elif p == 0 and soma % 2 == 1 and r == 0 and a == 0:
    print("Jogador 1 ganha!")
elif p == 0 and soma % 2 == 0 and r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif p == 0 and soma % 2 == 0 and r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif p == 0 and soma % 2 == 1 and r == 0 and a == 1:
    print("Jogador 1 ganha!")
elif p == 0 and soma % 2 == 1 and r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif p == 0 and soma % 2 == 1 and r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif p == 0 and soma % 2 == 0 and r == 0 and a == 1:
    print("Jogador 1 ganha!")








