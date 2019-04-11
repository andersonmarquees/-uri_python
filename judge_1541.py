from math import sqrt


def calcula_terreno(ladoA, ladoB, porc):

    cal = ((ladoA * ladoB) * 100) / porc
    tam = int(sqrt(cal))

    return print(tam)


while True:
    entrada = input().split()
    if entrada[0] == '0':
        break
    ladoA = int(entrada[0])
    ladoB = int(entrada[1])
    porc = int(entrada[2])
    calcula_terreno(ladoA, ladoB, porc)




