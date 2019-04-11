while True:
    t = ""
    n = int(input())
    if n == 0:
        break
    for i in range(0, n):

        t += str(i + 1) + " "

    print(t[:-1])

