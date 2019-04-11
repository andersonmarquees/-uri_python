import math
teste = int(input())
while teste > 0:

    entrada = input().split()
    n = int(entrada[0])
    m = int(entrada[1])

    i = m * math.log10(n) + 1
    print(int(i))

    teste -= 1

