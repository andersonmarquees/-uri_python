n = int(input())

while n > 0:

    bonus = int(input())

    dabriel = list(map(int, input().split()))
    at1 = dabriel[0]
    de1 = dabriel[1]
    level1 = dabriel[2]

    if level1 % 2 == 0:
        bon1 = bonus
    else:
        bon1 = 0

    valor_golpe_dabriel = ((at1 + de1) / 2) + bon1

    guarte = list(map(int, input().split()))
    at2 = guarte[0]
    de2 = guarte[1]
    level2 = guarte[2]

    if level2 % 2 == 0:
        bon2 = bonus
    else:
        bon2 = 0

    valor_golpe_guarte = ((at2 + de2) / 2) + bon2

    if valor_golpe_dabriel > valor_golpe_guarte:
        print('Dabriel')

    elif valor_golpe_guarte > valor_golpe_dabriel:
        print('Guarte')

    else:
        print('Empate')
    n -= 1



