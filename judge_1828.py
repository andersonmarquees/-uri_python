test = int(input())
cont = 0
while test > 0:
    entrada = input().split()
    sheldon = str(entrada[0])
    raj = str(entrada[1])

    if sheldon == 'tesoura' and raj == 'tesoura' or sheldon == 'papel' and raj == 'papel' or sheldon == 'pedra' and \
            raj == 'pedra' or sheldon == 'lagarto' and raj == 'lagarto' or sheldon == 'Spock' and raj == 'Spock':
        cont += 1
        print('Caso #{}: De novo!'.format(cont))

    elif sheldon == 'tesoura' and raj == 'papel' or sheldon == 'tesoura' and raj == 'lagarto':
        cont += 1
        print('Caso #{}: Bazinga!'.format(cont))
    elif sheldon == 'papel' and raj == 'tesoura' or sheldon == 'lagarto' and raj == 'tesoura':
        cont += 1
        print('Caso #{}: Raj trapaceou!'.format(cont))

    elif sheldon == 'papel' and raj == 'pedra' or sheldon == 'papel' and raj == 'Spock':
        cont += 1
        print('Caso #{}: Bazinga!'.format(cont))
    elif sheldon == 'pedra' and raj == 'papel' or sheldon == 'Spock' and raj == 'papel':
        cont += 1
        print('Caso #{}: Raj trapaceou!'.format(cont))

    elif sheldon == 'tesoura' and raj == 'lagarto' or sheldon == 'pedra' and raj == 'lagarto':
        cont += 1
        print('Caso #{}: Bazinga!'.format(cont))
    elif sheldon == 'lagarto' and raj == 'tesoura' or sheldon == 'lagarto' and raj == 'pedra':
        cont += 1
        print('Caso #{}: Raj trapaceou!'.format(cont))

    elif sheldon == 'pedra' and raj == 'tesoura' or sheldon == 'lagarto' and raj == 'Spock':
        cont += 1
        print('Caso #{}: Bazinga!'.format(cont))

    elif sheldon == 'tesoura' and raj == 'pedra' or sheldon == 'Spock' and raj == 'lagarto':
        cont += 1
        print('Caso #{}: Raj trapaceou!'.format(cont))

    elif sheldon == 'lagarto' and raj == 'papel' or sheldon == 'Spock' and raj == 'tesoura':
        cont += 1
        print('Caso #{}: Bazinga!'.format(cont))

    elif sheldon == 'papel' and raj == 'lagarto' or sheldon == 'tesoura' and raj == 'Spock':
        cont += 1
        print('Caso #{}: Raj trapaceou!'.format(cont))

    elif sheldon == 'Spock' and raj == 'pedra':
        cont += 1
        print('Caso #{}: Bazinga!'.format(cont))

    elif sheldon == 'pedra' and raj == 'Spock':
        cont += 1
        print('Caso #{}: Raj trapaceou!'.format(cont))

    test -= 1

