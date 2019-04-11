n = int(input())
entrada = list(map(int, input().split()))
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

for i in entrada:
    if i % 2 == 0:
        cont2 += 1

    if i % 3 == 0:
        cont3 += 1

    if i % 4 == 0:
        cont4 += 1

    if i % 5 == 0:
        cont5 += 1

print("{} Multiplo(s) de {}".format(cont2, 2))
print("{} Multiplo(s) de {}".format(cont3, 3))
print("{} Multiplo(s) de {}".format(cont4, 4))
print("{} Multiplo(s) de {}".format(cont5, 5))
