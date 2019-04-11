t = int(input())
while t > 0:
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])
    ga = float(entrada[2])
    gb = float(entrada[3])

    cont = 0
    while a <= b:

        a = int(((a * ga) / 100) + a)
        b = int(((b * gb) / 100) + b)
        cont += 1

        if cont > 100:
            break

    if cont > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(cont))
    t -= 1
