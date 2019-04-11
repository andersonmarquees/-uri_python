"""Will's Message"""


test = True
while test:
    try:
        _string = [y for y in input()]
        number = [int(num) for num in range(1, 27)]
        dic = dict(zip(number, _string))

        num = int(input())
        val = [int(num) for num in input().split()]

        for k in val:
            if k in dic.keys():
                print(dic[k], end='')
            else:
                pass
        dic.clear()
        print()

    except EOFError:
        test = False