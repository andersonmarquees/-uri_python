n = int(input())

while n > 0:
    num = int(input())

    if num % 2 == 0:
        soma = (2 * num) - 2
        print(soma)
    else:
        soma = (2 * num) - 1
        print(soma)

    n -= 1
    if n == 0:
        n = int(input())
    if num == 0:
        break




