a = 7
b = 4
for i in range(1, 10, 2):

    for j in range(a, b, -1):

        print('I={} J={}'.format(i, j))
    a += 2
    b += 2
