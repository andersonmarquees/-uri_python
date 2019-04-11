test = True
while test:
    n = list(map(int, input().split()))
    if n[0] == 0 and n[1] == 0:
        test = False
        break
    x = n[0]
    m = n[1]
    exp = x * m
    print(exp)


