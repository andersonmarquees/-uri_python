n = int(input())
total_bean = 0
while n > 0:
    bean = int(input())
    for i in range(0, bean):
        total_bean += 2 ** i
    kg = (total_bean // 12) // 1000
    print("{:.0f} kg".format(kg))
    total_bean = 0
    n -= 1


