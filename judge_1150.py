def chama(x):
    z = int(input())
    while z <= x:
        z = int(input())
    calcula(x, z)


def calcula(x, z):
    soma = x
    cont = 0
    while True:
        x += 1
        cont += 1
        soma += x
        if soma > z:
            break
    return print(cont + 1)


chama(int(input()))
