k = True
try:
    while k:
        entrada = input().split(':')
        hora = int(entrada[0])
        minuto = int(entrada[1])
        try:
            at = ((hora * 60) + minuto) + 60
            if at > 480:
                later = abs(480 - at)
                print("Atraso maximo: {}".format(later))
            else:
                later = 0
                print("Atraso maximo: {}".format(later))
        except:
            k = False
except EOFError:
    k = False
