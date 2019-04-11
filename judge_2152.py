n = int(input())

while n > 0:
    number = list(map(int, input().split()))
    if number[2] == 0 and number[0] >= 10 and number[1] >= 10:
        print("{}:{} - A porta fechou!".format(number[0], number[1]))
    elif number[2] == 1 and number[0] >= 10 and number[1] >= 10:
        print("{}:{} - A porta abriu!".format(number[0], number[1]))

    elif number[2] == 0 and number[0] < 10 and number[1] < 10:
        print("0{}:0{} - A porta fechou!".format(number[0], number[1]))
    elif number[2] == 1 and number[0] < 10 and number[1] < 10:
        print("0{}:0{} - A porta abriu!".format(number[0], number[1]))

    elif number[2] == 0 and number[0] < 10:
        print("0{}:{} - A porta fechou!".format(number[0], number[1]))
    elif number[2] == 1 and number[0] < 10:
        print("0{}:{} - A porta abriu!".format(number[0], number[1]))

    elif number[2] == 0 and number[1] < 10:
        print("{}:0{} - A porta fechou!".format(number[0], number[1]))
    elif number[2] == 1 and number[1] < 10:
        print("{}:0{} - A porta abriu!".format(number[0], number[1]))

    n -= 1





