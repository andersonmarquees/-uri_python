a = int(input())
b = int(input())

if a < b:
    for i in range(a+1, b):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
else:
    if a > b:
        for j in range(b+1, a):
            if j % 5 == 2 or j % 5 == 3:
                print(j)


