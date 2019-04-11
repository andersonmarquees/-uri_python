n = int(input())
while n > 0:
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    if y == 0:
        try:
            div = x / 0
            break
        except ZeroDivisionError:
            print("divisao impossivel")
    else:
        div = x / y
        print(div)
    n -= 1

"""
Trecho de codigo retirado da documentação do python;

 def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print "division by zero!"
     else:
         print "result is", result
     finally:
         print "executing finally clause"
"""