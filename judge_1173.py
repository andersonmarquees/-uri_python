lista = []
for i in range(0, 10):

    if i == 0:
        n = int(input())
        lista.append(n)
    else:
        lista.append(n * 2)
        n = n * 2

for j, k in enumerate(lista):
    print("N[{}] = {}".format(j, k))




