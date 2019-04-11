def fibonacci(n):
    lista = []
    if n == 0:
        print(n)
    f1, f2 = 0, 1
    while n > 0:
        print('{}'.format(f1), end=' ')
        f1, f2 = f2, f1 + f2
        lista.append(f1)
        n -= 1


fibonacci(int(input()))




