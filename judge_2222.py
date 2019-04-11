num_inst = int(input())
imprime = []
for k in range(num_inst):
    num_conj = int(input())
    lista = []

    for i in range(num_conj):
        lista.append(set([int(x) for x in input().split()[1:]]))

    operacao = int(input())
    for j in range(operacao):
        op_conj = [int(x) for x in input().split()]

        if op_conj[0] == 1:
            imprime.append(len(lista[op_conj[1] - 1] & lista[op_conj[2] - 1]))
        else:
            imprime.append(len(lista[op_conj[1] - 1] | lista[op_conj[2] - 1]))
for p in imprime:
    print(p)


