

x = int(input())
if x == 365:
    ano = x
    mes = 0
    dias = 0
else:
    if x > 365:
        ano = x // 365
        mes = (x % 365) // 30
        dias = (x % 365) % 30
    elif x < 365:
        ano = 0
        mes = x // 30
        dias = x % 30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, dias))
