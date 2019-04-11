lista = []


def cria_lista():

    for i in range(0, 20):
        n = int(input())
        lista.append(n)
    lista.reverse()

    return lista


def lista_reversa():
    cria_lista()
    for j, k in enumerate(lista):
        print("N[{}] = {}".format(j, k))


lista_reversa()


