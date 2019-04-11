mat = []


def cria_matriz(num):
    for i in range(1, num + 1):
        lin = []
        for j in range(1, num + 1):
            lin.append(j)
        mat.append(lin)
    return mat


def imprime_matriz():
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == j:
                print("{:3}".format(1), end='')

            elif j == 1:
                print("{:3}".format(i), end='')

            elif i == 1:
                print("{:3}".format(j), end='')

            elif i == num or i > j > 1:
                print("{:3}".format(i - j + 1), end='')

            elif j == num or j > i > 1:
                print("{:3}".format(j - i + 1), end='')
            if j < num:
                print(' ', end='')
        print()
    print()


while True:
    num = int(input())
    if num == 0:
        break
    cria_matriz(num)
    imprime_matriz()






















