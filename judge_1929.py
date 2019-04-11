n = list(map(int, input().split()))

if abs(n[0] - n[1]) < n[2] < n[0] + n[1] or abs(n[0] - n[1]) < n[3] < (n[0] + n[1]):
    print("S")
elif abs(n[1] - n[2]) < n[0] < (n[1] + n[2]) or abs(n[1] - n[2]) < n[3] < (n[1] + n[2]):
    print("S")
elif abs(n[2] - n[3]) < n[0] < (n[2] + n[3]) or abs(n[2] - n[3]) < n[1] < (n[2] + n[3]):
    print("S")
elif abs(n[0] - n[3]) < n[1] < (n[0] - n[3]) or abs(n[0] - n[3]) < n[2] < (n[0] - n[3]):
    print("S")
elif abs(n[1] - n[3]) < n[2] < (n[1] + n[3]) or abs(n[1] - n[3]) < n[0] < (n[1] + n[3]):
    print("S")
else:
    print("N")


