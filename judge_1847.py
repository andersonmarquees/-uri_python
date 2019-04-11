entrada = input().split()
a, b, c = int(entrada[0]), int(entrada[1]), int(entrada[2])

if a > b <= c:  # 1
    print(':)')
elif a < b >= c:  # 2
    print(':(')
elif a < b < c and abs(b - c) < abs(a - b):  # 3
    print(':(')
elif a < b < c and abs(b - c) >= abs(a - b):  # 4
    print(':)')
elif a > b > c and abs(b - c) < abs(a - b):  # 5
    print(':)')
elif a > b > c and abs(b - c) >= abs(a - b):  # 6
    print(':(')
elif a == b < c:
    print(':)')
else:
    if a == b >= c:
        print(':(')









