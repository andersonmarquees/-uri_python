lista = list(map(int, input().split()))
soma = total = valor = n = 0

for i in lista:
    if i == lista[0]:
        valor = i
    else:
        if i > 0:
            n = i
            break
for i in range(n):
    soma = valor + i
    total += soma
print(total)




