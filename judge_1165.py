def calcula_primo(x):
    soma = 0
    for i in range(1, x + 1):
        if x % i == 0:
            soma += 1
    if soma == 2:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
    return


def loop(n):

    while n > 0:
        x = int(input())
        calcula_primo(x)
        n -= 1


loop(int(input()))
