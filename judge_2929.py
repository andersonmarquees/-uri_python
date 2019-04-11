pilha = []


def push():
    n = int(input())

    while n > 0:
        b = input().upper().split()
        if b[0] == 'MIN':
            consulta()
        elif b[0] == 'POP':
            retira()
        else:
            pilha.append(int(b[1]))
        n -= 1


def consulta():

    min_value = pilha[0]

    if len(pilha) == 0:
        print("EMPYT")
    else:
        for value in pilha:
            if value < min_value:
                min_value = value
        return print(min_value)


def retira():
    if len(pilha) == 0:
        print("EMPYT")
    else:
        return pilha.pop()


push()