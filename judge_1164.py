def calcula_perfeito(x):

    soma = 0
    for i in range(1, x):
        if x % i == 0:
            soma += i
    if soma == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))

    return


def loop(n):

    while n > 0:
        x = int(input())
        calcula_perfeito(x)
        n -= 1


loop(int(input()))









