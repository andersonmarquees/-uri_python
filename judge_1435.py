while True:
    num = int(input())
    if num == 0:
        break

    mat = []

    for i in range(1, num + 1):
        lin = []
        for j in range(1, num + 1):
            lin.append(1)
        mat.append(lin)

    for i in range(1, num + 1):
        for j in range(1, num + 1):
            centro = i
            if j < centro:
                centro = j
            if num - i + 1 < centro:
                centro = num - i + 1
            if num - j + 1 < centro:
                centro = num - j + 1
            print("{:3}".format(centro), end='')
            if j < num:
                print(' ', end='')
        print()
    print()



