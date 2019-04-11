test = True
while test:
    try:
        n = int(input())
        i, j = 1, 1
        while i % n != 0:
            i = (10 * i + 1) % n
            j += 1
        print(j)
    except EOFError:
        test = False

