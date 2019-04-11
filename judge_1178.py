lista = []
x = float(input())
aux = x

for i in range(100):
    lista.append(aux)
    aux /= 2

for j, k in enumerate(lista):
    print("N[{}] = {:.4f}".format(j, float(k)))

