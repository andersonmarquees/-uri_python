mat = []


def cria_matriz(num):
    aux = 1
    for i in range(num):
        if i == 0:
            linha = []
            for j in range(num):
                linha.append(2 ** j)
            mat.append(linha)
        else:
            linha = []
            for j in range(num):
                linha.append(2 ** (j + aux))
            mat.append(linha)
            aux += 1
    return


def imprime(mat):
    t = len(str(mat[num - 1][num - 1]))
    for i in range(num):
        for j in range(num):
            mat[i][j] = str(mat[i][j])
            while len(mat[i][j]) < t:
                mat[i][j] = ' ' + mat[i][j]
        m = ' '.join(mat[i])

        print(m)
    print()


while True:
    num = int(input())
    if num == 0:
        break
    cria_matriz(num)
    imprime(mat)
    mat = []





















