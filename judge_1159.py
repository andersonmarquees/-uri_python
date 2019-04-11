while True:
    x = int(input())
    if x == 0:
        break
    soma = 0
    if x % 2 == 0:
        for i in range(x, x + 9, 2):
            soma += i
        print(soma)
    elif x % 2 == 1:
        for j in range(x + 1, x + 11, 2):
            soma += j
        print(soma)




