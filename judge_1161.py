def fatorial(m):

    if m == 0 or m == 1:
        return 1
    else:
        return m * fatorial(m - 1)


def fatorial2(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


test = True
while test:
    try:
        m, n = [int(num) for num in input().split()]
        print(fatorial(m) + fatorial(n))
    except EOFError:
        test = False



