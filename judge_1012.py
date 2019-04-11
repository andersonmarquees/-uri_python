

medidas = input().split()
A, B, C = float(medidas[0]), float(medidas[1]), float(medidas[2])
TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * pow(C, 2)
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = pow(B, 2)
RETANGULO = A * B
print("TRIANGULO: {:.3f}".format(TRIANGULO))
print("CIRCULO: {:.3f}".format(CIRCULO))
print("TRAPEZIO: {:.3f}".format(TRAPEZIO))
print("QUADRADO: {:.3f}".format(QUADRADO))
print("RETANGULO: {:.3f}".format(RETANGULO))
