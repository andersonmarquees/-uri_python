n = int(input())
result = 0
while n > 0:
    name = input()
    grau_dificuldade = float(input())

    notas = list(map(float, input().split()))
    notas.remove(max(notas))
    notas.remove(min(notas))
    result = sum(notas) * grau_dificuldade
    print("{} {:.2f}".format(name, result))
    n -= 1



