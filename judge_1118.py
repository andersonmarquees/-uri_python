def valida():
    n1 = float(input())
    while n1 < 0 or n1 > 10:
        print("nota invalida")
        n1 = float(input())

    n2 = float(input())
    while n2 < 0 or n2 > 10:
        print("nota invalida")
        n2 = float(input())
    print("media = {:.2f}".format((n1 + n2) / 2))
    return escolha()


def escolha():

    while True:
        op = float(input("novo calculo (1-sim 2-nao)\n"))
        while op != 1 and op != 2:
            op = float(input("novo calculo (1-sim 2-nao)\n"))

        if op == 1:
            valida()

        else:
            if op == 2:
                break
        break


valida()









