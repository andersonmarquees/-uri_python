numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
i = 0
n = int(input())
while n > 0:
    if n >= numeros[i]:
        print(letras[i].upper(), end='')
        n -= numeros[i]
    else:
        i += 1
print()










