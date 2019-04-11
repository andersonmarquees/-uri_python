from math import sqrt, cos, sin

test = True
g = 9.80665
pi = 3.14159
while test:
    try:
        heigth = float(input())
        p1, p2 = [int(num) for num in input().split()]  # Começo e fim da cidade
        number_chance = int(input())
        for i in range(number_chance):
            angle, speed = [float(x) for x in input().split()]
            rad = (angle * 3.14159) / 180

            begin_city = min(p1, p2)
            end_city = max(p1, p2)
            #_range = (pow(speed, 2) * sin(2 * rad)) / g
            # y = y + vt - 1/2g * t²
            a = -g / 2
            b = speed * sin(rad)
            c = heigth
            time = (- b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            _range = speed * time * cos(rad)

            if end_city >= _range >= begin_city:
                print("{:.5f} -> DUCK".format(_range))
            else:
                print("{:.5f} -> NUCK".format(_range))

    except EOFError:
        test = False


