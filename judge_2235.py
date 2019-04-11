valores = list(map(int, input().split()))
a = valores[0]
b = valores[1]
c = valores[2]


if a == b or b == c or a == c:
    print('S')
elif a + b == c or a + c == b or b + c == a:
    print('S')
else:
    print('N')


