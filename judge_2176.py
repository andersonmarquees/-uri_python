lista = []
n = input()
m = n.count('1')
if m % 2 == 0:
    n += '0'
    print(n)
else:
    n += '1'
    print(n)

