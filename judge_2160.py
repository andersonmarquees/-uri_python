def limitador(caractere):

    total = ''
    total += str(caractere)
    k = len(total)
    
    if k > 80:
        return print("NO")
    else:
        return print("YES")


n = input()
limitador(n)


