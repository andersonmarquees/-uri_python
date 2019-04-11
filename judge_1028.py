def calc_mdc(number1, number2):

    if number1 >= number2:
        aux = number1 % number2
        if aux == 0:
            return print(number2)
        return calc_mdc(number2, aux)

    else:
        aux = number2 % number1
        if aux == 0:
            return print(number1)

        return calc_mdc(number1, aux)


n = int(input())
while n > 0:
    values = list(map(int, input().split()))
    number1 = values[0]
    number2 = values[1]
    calc_mdc(number1, number2)
    n -= 1
