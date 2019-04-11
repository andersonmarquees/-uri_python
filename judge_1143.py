import math

n = int(input())
if 1 < n < 1000:
    for i in range(1, n+1):
        quadrado = math.pow(i, 2)
        cubo = math.pow(i, 3)
        print("{:.0f} {:.0f} {:.0f}".format(i, quadrado, cubo))


