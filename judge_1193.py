def change_base(number, _string):

    if _string == 'bin':
        dec = int(number, 2)
        num = number
        valor = 0
        for i in num:
            valor = valor * 2 + int(i)
        print("{} dec".format(dec))
        print("{} hex".format(hex(valor)[2:]))
        print()

    if _string == 'dec':
        _hex = hex(int(number))
        _bin = bin(int(number))
        print("{} hex".format(_hex[2:]))
        print("{} bin".format(_bin[2:]))
        print()

    if _string == 'hex':
        dec = int(number, 16)
        _bin = bin(dec)
        print("{} dec".format(dec))
        print("{} bin".format(_bin[2:]))
        print()


n = int(input())
cont = 0
while n > 0:

    values = list(map(str, input().split()))
    number = values[0]
    _string = values[1].lower()
    cont += 1
    print("Case {}:".format(cont))
    change_base(number,  _string)

    n -= 1







