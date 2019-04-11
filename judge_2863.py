test = True
try:
    lista = []
    while test:
        n = int(input())
        for i in range(n):
            bateria = float(input())
            lista.append(bateria)
        print(min(lista))
        lista = []
except EOFError:
    test = False




