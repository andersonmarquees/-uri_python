test = True
try:
    while test:
        entrada = list(map(int, input().split()))
        soma = entrada[0] ^ entrada[1]
        print(soma)
except EOFError:
    test = False









