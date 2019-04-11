def calcula(n):

    if max(n) < 10:
        print(1)
    elif 10 < max(n) < 20:
        print(2)
    else:
        if max(n) >= 20:
            print(3)


while True:
    try:
        L = int(input())
        if 1 <= L <= 500:
            entrada = input().split()
            n = [int(i) for i in entrada]
            calcula(n)
    except EOFError:
        break




