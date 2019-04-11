medidas = input().split()
X, Y = int(medidas[0]), int(medidas[1])
if X == 1:
    valor = Y * 4.00
    print("Total: R$ {:.2f}".format(valor))
elif X == 2:
    valor = Y * 4.50
    print("Total: R$ {:.2f}".format(valor))
elif X == 3:
    valor = Y * 5.00
    print("Total: R$ {:.2f}".format(valor))
elif X == 4:
    valor = Y * 2.00
    print("Total: R$ {:.2f}".format(valor))
elif X == 5:
    valor = Y * 1.50
    print("Total: R$ {:.2f}".format(valor))
