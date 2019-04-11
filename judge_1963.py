entrada = list(map(float, input().split()))
porc = ((entrada[1] * 100) / entrada[0]) - 100
print('{:.2f}%'.format(porc))



