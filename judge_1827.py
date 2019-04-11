def cria_matriz():

    mat = []

    num = int(input())
    for i in range(num):
        lin = []
        for j in range(num):
            lin.append(0)
        mat.append(lin)
    return num, mat


def diagonal(num, mat):
    for i in range(num):
        for j in range(num):
            if i == j:
                mat[i][j] = 2
            if i + j == num -1:
                mat[i][j] = 3
    return mat


def matrix_1(num, mat):
    for i in range(num // 3, num - num // 3):
        for j in range(num // 3, num - num // 3):
            mat[i][j] = 1
    return mat


def matrix_4(num, mat):
    for i in range(num):
        for j in range(num):
            if i == j and i + j == num - 1:
                mat[i][j] = 4
    return mat


def impreme(num, mat):
    for i in range(num):
        for j in range(num):
            print(mat[i][j], end='')
        print()
    print()
    return mat


test = True
while test:
    try:
        num, mat = cria_matriz()
        mat = diagonal(num, mat)
        mat = matrix_1(num, mat)
        mat = matrix_4(num, mat)
        mat = impreme(num, mat)
    except EOFError:
        test = False





