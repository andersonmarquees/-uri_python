def imprime():

    if maior >= 8.0:
        return print(num)
    else:
        return print("Minimum note not reached")


n = int(input())
maior = 0
for i in range(n):
    entrada = input().split()

    numero = int(entrada[0])

    notas = float(entrada[1])

    if notas > maior:
        maior = notas
        num = numero
imprime()






