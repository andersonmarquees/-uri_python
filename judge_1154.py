idade = cont = 0
while True:
    n = int(input())
    if n < 0:
        break
    idade += n
    cont += 1
    media = idade / cont
print("{:.2f}".format(media))



