
N = int(input())
if N >= 3600:
    hora = N // 3600
    mim = (N % 3600) // 60
    seg = (N % 3600) % 60
else:
    if N < 3600:
        hora = 0
        mim = N // 60
        seg = N % 60
print("{}:{}:{}".format(hora, mim, seg))
