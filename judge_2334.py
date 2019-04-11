test = True
tot = 0
while test:
    n = int(input())
    if n == 0:
        print("0")
    elif n != -1 and n != 0:
        tot = n - 1
        print(tot)
    if n == -1:
        test = False


