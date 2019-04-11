def base(n):
    global value
    for caractere in n:

        if 'x' not in n:
            aux = int(n)
            value = hex(aux).upper()[2:]
            return print('0x{}'.format(value))
        else:
            value = int(n, 16)
            return print(value)


while True:
    n = input()
    if '-' in n:
        break
    base(n)




