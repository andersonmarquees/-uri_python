def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat = fat * i

    return print(fat)


fatorial(int(input()))

