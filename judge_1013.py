


medidas = input().split()
a, b, c = int(medidas[0]), int(medidas[1]), int(medidas[2])
r = ((a + b) + abs(a - b)) / 2
f = ((r + c) + abs(r - c)) / 2
print("{:.0f} eh o maior".format(f))
