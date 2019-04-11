coluna = int(input())
op = input().upper()

matriz = []
soma = 0

for i in range(12):
    line = []
    for j in range(12):
        valor = float(input())
        line.append(valor)
    matriz.append(line)

for i in range(12):
    soma += matriz[i][coluna]

if op == 'S':
    print("{}".format(soma))
else:
    print("{:.1f}".format(soma / 12))
