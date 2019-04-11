from math import sqrt
data = input().split()
A, B, C = float(data[0]), float(data[1]), float(data[2])
d = pow(B, 2) - 4 * A * C
if d < 0 or A == 0:
    print("Impossivel calcular")
else:
    R1 = (- B + (sqrt(d))) / (2 * A)
    R2 = (- B - (sqrt(d))) / (2 * A)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1, R2))
