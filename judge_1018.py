

N = int(input())
if 0 < N < 1000000:
    print(N)
    a = N // 100
    N = N % 100
    print("{} nota(s) de R$ 100,00".format(a))
    b = N // 50
    N = N % 50
    print("{} nota(s) de R$ 50,00".format(b))
    c = N // 20
    N = N % 20
    print("{} nota(s) de R$ 20,00".format(c))
    d = N // 10
    N = N % 10
    print("{} nota(s) de R$ 10,00".format(d))
    e = N // 5
    N = N % 5
    print("{} nota(s) de R$ 5,00".format(e))
    f = N // 2
    N = N % 2
    print("{} nota(s) de R$ 2,00".format(f))
    g = N // 1
    N = N % 1
    print("{} nota(s) de R$ 1,00".format(g))
