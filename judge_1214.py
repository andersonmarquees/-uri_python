case_test = int(input())

while case_test > 0:
    values = [int(num) for num in input().split()]
    num_students = values[0]
    media = sum(values[1:])
    up_media = float(media / values[0])
    cont = 0
    for i in values[1:]:
        if i > up_media:
            cont += 1
    final_media = float((cont * 100) / values[0])
    print("{:.3f}%".format(final_media))
    case_test -= 1


