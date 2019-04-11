op = input().upper()
mat = []
soma = 0
for i in range(12):
    lin = []
    for j in range(12):
        valores = float(input())
        lin.append(valores)
    mat.append(lin)

for i in range(1, 11):
    if i <= 5:
        for j in range(0, i):
            soma += mat[i][j]
    else:
        for j in range(0, 11 - i):
            soma += mat[i][j]


if op == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma / 30))

