while True:
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    if x == y:
        break
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")






