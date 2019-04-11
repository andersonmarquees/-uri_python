test = True
while test:
    try:
        n = int(input())
        n -= 1
        print(n)

    except EOFError:
        test = False



