def year_bissexto(year):

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("This is leap year.")
        huluculu(year)
        buluculu(year)

    elif year % 15 == 0:
        huluculu(year)

    else:
        print("This is an ordinary year.")


def huluculu(year):

    if year % 15 == 0:
        print("This is huluculu festival year.")


def buluculu(year):

    if year % 55 == 0:
        print("This is bulukulu festival year.")


i = 0
test = True
while test:
    try:
        if i:
            print('')
        i = 1
        year = int(input())
        year_bissexto(year)
    except EOFError:
        test = False
        break




