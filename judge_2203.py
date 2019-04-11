from math import sqrt, pow
test = True
while test:
    try:
        values = [int(num) for num in input().split()]
        x = values[0]
        y = values[1]
        a = values[2]
        b = values[3]
        v = values[4]
        r1 = values[5]
        r2 = values[6]

        space = v * 1.5
        n = sqrt(pow((x - a), 2) + pow((y - b), 2)) + space
        skill = abs(r1 + r2)

        if skill >= n:
            print('Y')
        else:
            print('N')

    except EOFError:
        test = False




