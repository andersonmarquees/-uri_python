from math import sqrt, pow

pi = 3.1415926535897
test = True
while test:
    try:
        n = [int(num) for num in input().split()]
        a, b, c = n[0], n[1], n[2]

        raio = (a * b * c) / sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))

        # Area do circulo maior
        area_circulo_maior = pi * pow(raio, 2)

        # Area do triangulo
        p = (a + b + c) / 2
        area_triangulo = sqrt(p*(p-a)*(p-b)*(p-c))

        # Area do circulo menor

        area_area_circulo_menor = pow((area_triangulo/p), 2) * pi

        area_girassol = area_circulo_maior - area_triangulo
        area_violeta = area_triangulo - area_area_circulo_menor
        area_rosas = area_area_circulo_menor

        print("{:.4f} {:.4f} {:.4f}".format(area_girassol, area_violeta, area_rosas))

    except EOFError:
        test = False


