test = True
casos = 0
try:
    while test:
        n = input()
        casos += 1
        cont = len(n)
        seq = input()
        i = 0
        pos = 0
        contador = 0
        comparando = True
        while comparando:
            sequencia = seq[:cont]
            if sequencia == n:
                pos = i
                contador += 1
            seq = seq[1:]
            if sequencia == '':
                comparando = False
            i += 1
        if contador != 0:
            print("Caso #{}:\nQtd.Subsequencias: {}\nPos: {}".format(casos, contador, pos + 1))
        else:
            print("Caso #{}:\nNao existe subsequencia".format(casos))
        print('')
except EOFError:
    test = False





