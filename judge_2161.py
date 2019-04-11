n = int(input())
x = 0.0
for i in range(n):
    x += 6.0
    x = (1.0 / x)
x += 3.0
print("{:.10f}".format(x))

