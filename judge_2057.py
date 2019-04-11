saida = list(map(int, input().split()))

horario = saida[0] + saida[1] + saida[2]

if horario == 24:
    print(0)
elif horario > 24:
    horario -= 24
    print(horario)
elif horario < 0:
    horario += 24
    print(horario)
else:
    print(horario)


