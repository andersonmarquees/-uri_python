lista = []

for i in range(0, 100):
    n = float(input())
    lista.append(n)
for j, k in enumerate(lista):
    if k <= 10:
        print("A[{}] = {:.1f}".format(j, k))

