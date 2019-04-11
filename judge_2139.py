import datetime
test = True
try:
    while test:
        entrada = list(map(int, input().split()))
        ano = 2016
        dia = entrada[0]
        mes = entrada[1]
        hoje = datetime.date(ano, dia, mes)
        natal = datetime.date(2016, 12, 25)
        f = (natal - hoje).days
        if f == 1:
            print("E vespera de natal!")
        elif f == 0:
            print("E natal!")
        elif f < 1:
            print("Ja passou!")
        else:
            print("Faltam {} dias para o natal!".format(f))

except EOFError:
    test = False


