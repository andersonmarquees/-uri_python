import math

n = int(input())

minino = (n / math.log(n))
maximo = 1.25506 * (n / math.log(n))

print("{:.1f} {:.1f}".format(minino, maximo))
