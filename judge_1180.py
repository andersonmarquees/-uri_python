n = int(input())

x = input().split()
x = [int(i) for i in x]
p = 0
for i in range(n):
    if i == 0:
        menor = x[0]
    else:
        if x[i] < menor:
            menor = x[i]
            p = i
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(p))


#  m, n = list(map(int, input().split()))


'''entrada = input().split()
x = (int(i) for i in entrada)
print(list(x))'''
