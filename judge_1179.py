par = []
impar = []

for j in range(15):
    valor = int(input())

    if valor % 2 == 0:
        par.append(valor)
        if len(par) == 5:
            for i, k in enumerate(par):
                print("par[{}] = {}".format(i, k))
                par = []
    elif valor % 2 == 1:
        impar.append(valor)
        if len(impar) == 5:
            for l, k in enumerate(impar):
                print("impar[{}] = {}".format(l, k))
                impar = []

for l, k in enumerate(impar):
    print("impar[{}] = {}".format(l, k))
for i, k in enumerate(par):
    print("par[{}] = {}".format(i, k))

