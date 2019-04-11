from math import pow


def triangulo(a, b, c):

    if abs(b - c) < a < b + c or abs(a - c) < b < a + c or abs(a - b) < c < a + b:
        retangulo()
    else:
        print("Invalido")


def retangulo():

    if pow(a, 2) == pow(b, 2) + pow(c, 2) or pow(b, 2) == pow(a, 2) + pow(c, 2) or pow(c, 2) == pow(b, 2) + pow(a, 2):
        return tipo(a, b, c), print("Retangulo: S")

    else:
        return tipo(a, b, c), print("Retangulo: N")


def tipo(a, b, c):

    if a == b == c:
        return print("Valido-Equilatero")
    elif a != b and b != c and a != c:
        return print("Valido-Escaleno")
    elif a == b != c or a == c != b or b == c != a:
        return print("Valido-Isoceles")


values = list(map(int, input().split()))
a = values[0]
b = values[1]
c = values[2]

triangulo(a, b, c)


