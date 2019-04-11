op = input().upper()

matriz = []

for i in range(12):
    line = []
    for j in range(12):
        valores = float(input())
        line.append(valores)
    matriz.append(line)
a = 5
b = 7
soma = 0
for i in range(7, 12):
    for j in range(a, b):
        soma += matriz[i][j]
    a -= 1
    b += 1

if op == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma / 30))




