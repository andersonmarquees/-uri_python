numero = int(input())
lista = []
while True:

    lista.append(numero % 10)
    numero = numero // 10

    if numero == 0:
        break
for i in lista:
    print(i, end='')
print('')




