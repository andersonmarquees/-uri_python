

from math import sqrt
medidas1 = input().split()
x1, y1 = float(medidas1[0]), float(medidas1[1])
medidas2 = input().split()
x2, y2 = float(medidas2[0]), float(medidas2[1])
distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print("{:.4f}".format(distance))
