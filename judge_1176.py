lista = [0]


def cria_fib():
    a, b = 0, 1
    for i in range(60):
        a, b = b, a + b
        lista.append(a)
    return lista


def imprime():
    cria_fib()
    t = int(input())
    for i in range(t):
        fib = int(input())
        print("Fib({}) = {}".format(fib, lista[fib]))


imprime()
