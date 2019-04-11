notas = [100, 50, 20, 10, 5, 2]
total = 0
while True:
    entrada = list(map(int, input().split()))
    troco = entrada[1] - entrada[0]
    if entrada[0] == 0 and entrada[1] == 0:
        break
    #print(troco)
    for nota in range(len(notas)):
        if troco == 100 or troco == 20:
            total = 2
        else:
            num_nota = troco // notas[nota]
            troco -= num_nota * notas[nota]
            total += num_nota

    #print(troco)
    if total == 2:
        print("possible")
    else:
        print("impossible")
    total = 0




