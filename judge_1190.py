op = input().upper()
soma = 0
mat = []

for i in range(12):
    lin = []
    for j in range(12):
        valores = float(input())
        lin.append(valores)
    mat.append(lin)

a = 11
b = 10
for i in range(1, 11):
    if i <= 5:
        for j in range(a, b, -1):
            soma += mat[i][j]
        b -= 1
    else:
        for j in range(i + 1, 12):
            soma += mat[i][j]

if op == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma / 30))




