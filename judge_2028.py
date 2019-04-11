lista = [0]
test = True
cont = 0
num = 0
try:
    while test:
        num = 1
        n = int(input())
        cont += 1
        if n == 0:
            print("Caso {}: 1 numero".format(cont))
        else:
            for i in range(0, n + 1):
                for j in range(0, i):
                    num += 1
                    lista.append(i)

            print("Caso {}: {} numeros".format(cont, num))
        for k in range(len(lista) - 1):
            print(lista[k], end=' ')
        print(lista[len(lista) - 1])
        print()
        lista = [0]
except EOFError:
    test = False






# Uma forma criativa de tirar o espaço no fim da sequencia, que é imprimir no primeiro print toda a sequencia menos,
# o ultimo elemento, pois ele será impresso no print de baixo fora do (for), assim se tira o espaço.

'''lista = [0, 1, 2, 3]
for i in lista:
    print(i, end=' ')
print(lista[len(lista) - 1])'''
