n = int(input())
cont = 0
while n > 0:

    word = input()
    for i in word:
        cont += 1
    temp = cont * 0.01
    print('{:.2f}'.format(temp))
    cont = 0

    n -= 1




