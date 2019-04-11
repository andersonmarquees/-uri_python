tabela = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
rest = []
i = 0
n = int(input())
while n > 0:
    if n == nums[i]:
        print(tabela[i])
    else:
        rest.append(n % 16)
        n = n // 16

rest.reverse()
for j in rest:
    print(tabela[j], end='')

'''n = int(input())
print(hex(n).lstrip('0x').upper())'''


