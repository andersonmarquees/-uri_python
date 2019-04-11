test = True
while test:
    try:
        values = [int(number) for number in input().split()]
        soldier1 = values[0]
        soldier2 = values[1]

        sub = abs(soldier1 - soldier2)
        print(sub)

    except EOFError:
        test = False

