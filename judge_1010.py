


#  Novo com novo input
entrada1 = input().split()
valor1 = [float(i) for i in entrada1]

entrada2 = input().split()
valor2 = [float(j) for j in entrada2]

custo = (int(entrada1[1]) * float(entrada1[2])) + (int(entrada2[1]) * float(entrada2[2]))

print("VALOR A PAGAR: R$ {:.2f}".format(custo))

