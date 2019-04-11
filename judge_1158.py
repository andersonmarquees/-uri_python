def soma_par(n, m):
    soma = n + 1
    temp = 0
    while m != 0:
        temp += soma
        soma += 2
        m -= 1
    print(temp)


def soma_impar(n, m):
    soma = n
    temp = 0
    while m != 0:
        temp += soma
        soma += 2
        m -= 1
    print(temp)


x = int(input())
while x != 0:
    entrada = input().split()
    n = int(entrada[0])
    m = int(entrada[1])

    if n % 2 == 0:
        soma_par(n, m)
    else:
        soma_impar(n, m)
    x -= 1
