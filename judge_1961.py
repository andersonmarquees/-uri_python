entrada = input().split()
p = int(entrada[0])
n = int(entrada[1])
nums = list(map(int, input().split()))
cont = 0
for i in range(len(nums) - 1):
    if (abs(nums[i] - nums[i + 1])) > p:
        cont += 1

if cont >= 1:
    print("GAME OVER")
else:
    print("YOU WIN")


