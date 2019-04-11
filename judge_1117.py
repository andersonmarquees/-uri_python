soma = 0
total = 0

while total < 2:
    notas = float(input())
    if notas >= 0 and notas <= 10:
        soma += notas
        total += 1
    else:
        print("nota invalida")

print("media = {:.2f}".format(soma/2))


