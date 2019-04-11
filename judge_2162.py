n = int(input())
lista = list(map(int, input().split()))
aux = ''
for i in range(0, n - 1):
    if lista[i] == lista[i + 1]:
        aux += str(0)
    else:
        aux += str(1)

for j in range(2, n):
    if lista[j] >= lista[j - 1] >= lista[j - 2]:
        aux += str(0)
    elif lista[j] <= lista[j - 1] <= lista[j - 2]:
        aux += str(0)
    else:
        aux += str(1)

if '0' in aux:
    print(0)
else:
    print(1)






