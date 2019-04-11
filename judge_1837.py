numeros = input().split()
a = int(numeros[0])
b = int(numeros[1])

# a = bq + r
# r = a - bq
# q = a/b
# 0 <= r < |b|
# r = a % b

if b < 0 < a:  # a > 0 e b < 0 ok
    r = a % abs(b)
    q = int(a / b)
    print(q, r)
elif b > 0 > a:  # a < 0 e b > 0 ok
    q = a // b
    r = a - b * q
    print(q, r)

########################################
elif b < 0 > a:  # a < 0 e b < 0
    q = a / b
    r = a % b
    if r > 0:
        if q > 0:
            q = q

    if r < 0:
        q += 1
        r = a - (b * int(q))
    print(int(q), r)

########################################

else:  # a > 0 e b > 0 ok
    q = int(a / b)
    r = a - b * q
    print(q, r)



