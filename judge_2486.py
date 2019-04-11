valores = {'suco': 120, 'morango': 85, 'mamao': 85, 'goiaba': 70, 'manga': 56, 'laranja': 50, 'brocolis': 34}


def vitamina(lista):

    soma = 0
    for j in lista:
        soma += j

    if soma >= 130:
        print("Menos {} mg".format(soma - 130))
    elif soma <= 110:
        print("Mais {} mg".format(110 - soma))
    else:
        print("{} mg".format(soma))


test = True
while test:
    lista = []
    qtd_food = int(input())
    if qtd_food == 0:
        test = False
        break
    for i in range(qtd_food):
        _input = list(map(str, input().split()))
        number = int(_input[0])
        name_food = _input[1]
        lista.append(valores[name_food] * number)
    vitamina(lista)





