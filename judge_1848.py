cont = 0
soma = 0
while cont != 3:
    entrada = input().split()

    if entrada[0] == 'caw' and entrada[1] == 'caw':
        print(soma)
        soma = 0
        cont += 1
    else:
        if entrada[0] == '---':
            soma += 0
        elif entrada[0] == '*--':
            soma += 4
        elif entrada[0] == '-*-':
            soma += 2
        elif entrada[0] == '--*':
            soma += 1
        elif entrada[0] == '**-':
            soma += 6
        elif entrada[0] == '***':
            soma += 7
        elif entrada[0] == '-**':
            soma += 3
        elif entrada[0] == '*-*':
            soma += 5












