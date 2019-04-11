x = int(input())
y = int(input())
soma = 0
if x > y:
    for i in range(x-1, y, -1):  # x > y pega o primeiro numero
        if i % 2 == 1:
            soma += i
    print(soma)
else:
    for j in range(x+1, y):  # x < y pega o primeiro numero
        if j % 2 == 1:
            soma += j
    print(soma)




