test = True
while test:
    try:
        values = [int(x) for x in input().split()]

        space = values[0] * (values[1] * 2)
        print(space)

    except EOFError:
        test = False

