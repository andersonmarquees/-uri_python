"""Quick prime"""

from math import sqrt


def prime(number):

    cont = 0
    if number == 2:
        return 'Prime'
    if number % 2 == 0:
        return 'Not Prime'
    if number == 1:
        return 'Not Prime'
    else:
        for j in range(3, int(sqrt(number) + 1)):

            if number % j == 0:
                cont += 1
                if cont > 2:
                    return 'Not Prime'
            j += 2
        if cont >= 1:
            return 'Not Prime'
        else:
            return 'Prime'


n = int(input())
while n > 0:
    number = int(input())
    print(prime(number))
    n -= 1







