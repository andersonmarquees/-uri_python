quadra = []


def cria_quadra(tam):

    for i in range(tam):
        lin = []
        for j in range(tam):
            lin.append(j)
        quadra.append(lin)
    print(quadra)


def imprime():

    for i in range(len(quadra)):
        for j in range(len(quadra[i])):
            print(j, end=' ')
        print()


tam = int(input())
cria_quadra(tam)
imprime()


