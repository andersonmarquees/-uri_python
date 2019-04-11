n = int(input())
while n > 0:
    entrada = input()
    lista = [int(x) for x in entrada.split()]
    m = min(lista)
    pos = lista.index(m)
    print(pos + 1)
    break










