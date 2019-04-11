n = int(input())
serie = [1001, 1002, 1003, 1004, 1005]
valor = [1.50, 2.50, 3.50, 4.50, 5.50]
i = 0
total = 0
while n > 0:
    entrada = list(map(int, input().split()))
    numero = entrada[0]
    qtd = entrada[1]

    if numero >= serie[i] or numero <= serie[i]:
        i = serie.index(numero)
        compra = qtd * valor[i]
        total += compra
    n -= 1
print("{:.2f}".format(total))





