n = int(input())
k = list(map(int, input().split()))
pos = 0

for i in range(0, n - 1):
    if k[i] > k[i + 1]:
        pos += i + 2
        break
    elif k[i] <= k[i + 1]:
        pos = 0
if pos != 0:
    print(pos)
else:
    print("0")




