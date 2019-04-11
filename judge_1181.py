n = int(input())  # linha a ser calculada a soma
op = input().upper()
soma = 0

matriz = []

for i in range(12):
    line = []
    for j in range(12):
        valor = float(input())
        line.append(valor)
    matriz.append(line)

for j in range(len(matriz)):
    soma += matriz[n][j]

if op == 'S':
    print("{}".format(soma))
else:
    print("{:.1f}".format(soma / 12))

