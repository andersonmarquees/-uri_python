entrada = list(map(int, input().split()))
qtd_cachorro_quente = entrada[0]
participantes = entrada[1]

media_consumo_cahorro_quente_por_pessoa = float(qtd_cachorro_quente / participantes)

print("{:.2f}".format(media_consumo_cahorro_quente_por_pessoa))



