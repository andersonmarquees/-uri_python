total_grenal = empates = vitoria_inter = vitoria_gremio = 0


def gols():

    global total_grenal, inter_gol, gremio_gol,  empates,  vitoria_inter, vitoria_gremio
    global vencedor

    inter_gol = gremio_gol = vencedor = 0

    while True:
        entrada = input().split()
        inter = int(entrada[0])
        gremio = int(entrada[1])

        total_grenal += 1  # total de grenal

        inter_gol += inter  # gols do inter
        gremio_gol += gremio  # gols do gremio

        #  Quantidade de empates
        if inter_gol == gremio_gol:
            empates += 1

        # Quantidade de vitorias do inter
        elif inter_gol > gremio_gol:
            vitoria_inter += 1

        #  Quantidade de vitorias do gremio
        elif gremio_gol > inter_gol:
            vitoria_gremio += 1

        #  vencedor
        if vitoria_inter > vitoria_gremio:
            vencedor = 'Inter venceu mais'
        elif vitoria_gremio > vitoria_inter:
            vencedor = 'Gremio venceu mais'
        elif vitoria_inter == vitoria_gremio:
            vencedor = "Nao houve vencedor"

        return escolha()


def escolha():

    while True:
        op = int(input("Novo grenal (1-sim 2-nao)\n"))
        while op != 1 and op != 2:
            op = int(input("Novo grenal (1-sim 2-nao)\n"))

        if op == 1:
            gols()
        else:
            if op == 2:
                break
        break


gols()

print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}\n{}".format(total_grenal, vitoria_inter, vitoria_gremio, empates,
                                                               vencedor))
