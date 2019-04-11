n = int(input())
if 1 < n < 1000:
    for i in range(1, n+1):
        square = pow(i, 2)
        cube = pow(i, 3)

        print(i, square, cube)
        print(i, square+1, cube+1)

