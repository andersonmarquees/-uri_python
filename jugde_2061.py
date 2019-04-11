nums = list(map(int, input().split()))
abas, acoes = nums[0], nums[1]
cont = abas
while acoes > 0:
    n = str(input()).lower()
    if n == 'fechou':
        cont += 1
    elif n == 'clicou':
        cont -= 1
    acoes -= 1
print(cont)



