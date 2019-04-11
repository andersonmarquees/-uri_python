lista = []
for j in range(0, 10):
    n = int(input())
    if n < 0 or n == 0:
        lista.append(1)
    else:
        lista.append(n)

for i, k in enumerate(lista):
    print('X[{}] = {}'.format(i, k))


'''class Vetor(object):
    def __int__(self):
        self.lista()
        self.imprime()

    def lista(self):
        lista = []
        for j in range(0, 5):
            n = int(input())
            if n < 0 or n == 0:
                lista.append(1)
            else:
                lista.append(n)
        return lista

    def imprime(self):
        lista = self.lista()
        for i, k in enumerate(lista):
            return print('X[{}] = {}'.format(i, k))


r = Vetor()
r.lista()
r.imprime()

# [1, 0, 3, 4, -3, 0, 7, -1, 4, 2]'''