entrada = input().split()
x = int(entrada[0])
y = int(entrada[1])
cont = 1

for i in range(1, (int((y/x) + 1))):
    t = ""
    for j in range(x):
        t += str(cont) + " "
        cont += 1
    print(t[:-1])
