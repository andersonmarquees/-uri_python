rodada = int(input())
aldo = beto = test = 0
while True:
    for i in range(0, rodada):
        v = input().split()
        a, b = int(v[0]), int(v[1])

        if a > b:
            aldo += a
        else: #  b > a:
            beto += b
    test += 1

    if aldo > beto:
        print("Teste {}\nAldo".format(test))
        print('')
    else:
        print("Teste {}\nBeto".format(test))
        print('')
    rodada = int(input())
    if rodada == 0:
        break
    aldo = beto = 0


