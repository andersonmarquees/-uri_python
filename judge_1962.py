n = int(input())
while n > 0:
    ano = int(input())
    if ano > 2014:
        print('{} A.C.'.format(ano - 2014))
    else:
        print('{} D.C.'.format(2015 - ano))
    n -= 1


