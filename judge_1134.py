Alcool = 0
Gasolina = 0
Diesel = 0
op = 0
while op != 4:
    op = int(input())

    if op == 1:
        Alcool += 1
    if op == 2:
        Gasolina += 1
    if op == 3:
        Diesel += 1

print("MUITO OBRIGADO")
print("Alcool: {}".format(Alcool))
print("Gasolina: {}".format(Gasolina))
print("Diesel: {}".format(Diesel))



