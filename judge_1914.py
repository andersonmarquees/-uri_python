def parImpar(nome, escolha, numero):

    if (jog1 + jog2) % 2 == 0 and escolha1 == 'PAR':
        print(jogador1)

    elif (jog1 + jog2) % 2 == 1 and escolha1 == 'IMPAR':
        print(jogador1)

    else:
        print(jogador2)


n = int(input())
while n > 0:
    nome = input().split()
    jogador1 = nome[0].title()
    escolha1 = nome[1]
    jogador2 = nome[2].title()
    escolha = nome[3]

    numero = input().split()
    jog1 = int(numero[0])
    jog2 = int(numero[1])

    parImpar(nome, escolha, numero)
    n -= 1

