cont = 0


def food(meal):

    global cont

    if meal == 1:
        return cont
    if meal < 1:
        return cont
    else:
        meal /= 2
        cont += 1
        return food(meal)


n = int(input())
while n > 0:

    meal = float(input())
    print("{} dias".format(food(meal)))
    cont = 0
    n -= 1

