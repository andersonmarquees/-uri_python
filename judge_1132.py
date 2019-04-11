x = int(input())
y = int(input())
soma = 0
if y > x:
    for i in range(x, y+1):
        if i % 13 != 0:
            soma += i
    print(soma)
else:
    for j in range(y, x+1):
        if j % 13 != 0:
            soma += j
    print(soma)


