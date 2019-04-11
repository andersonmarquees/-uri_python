soma = 1
t = 2
cont = 3
while cont < 40:
    soma += float(cont) / float(t)
    t *= 2
    cont += 2
print("{:.2f}".format(soma))
