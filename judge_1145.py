class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        per = self.a + self.b + self.c
        return per

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            if self.a != self.b != self.c:
                return 'escaleno'


t = Triangulo(1, 1, 3)
print(t.perimetro())

print(t.a)
print(t.b)
print(t.c)

print(t.tipo_lado())