op = input().upper()

matriz = []

for i in range(12):
    line = []
    for j in range(12):
        valores = float(input())
        line.append(valores)
    matriz.append(line)
soma  = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i + j > 11:
            soma += matriz[i][j]
if op == 'S':
    print("{}".format(soma))
else:
    print("{:.1f}".format(soma / 66))

