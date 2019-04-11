op = input().upper()

matriz = []

for i in range(12):
    line = []
    for j in range(12):
        valores = float(input())
        line.append(valores)
    matriz.append(line)

soma = 0
for i in range(0, 5):
    for j in range(i + 1, 11 - i):
        soma += matriz[i][j]


if op == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma / 30))


