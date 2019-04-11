from math import pow
test = True
try:
    while test:

        volume = float(input())
        d = float(input())

        pi = 3.14
        r = d / 2

        area = pi * pow(r, 2)
        h = volume / area

        print("ALTURA = {:.2f}".format(h))
        print("AREA = {:.2f}".format(area))

except EOFError:
    test = False



