# dimensoes do salão em metros
altura, largura = list(map(int, input().split()))

# largura das tábuas, em centímetros
l = int(input())

# o número de tábuas
k = int(input())

# cada um representando o comprimento, em metros, de uma tábua

comprimento = list(map(int, input().split()))


def calc_area_salao(altura, largura):
    """
    :param altura: do salão
    :param largura: do salão
    :return: area do salão
    """
    area = altura * largura
    return area


def calc_area_tabua(k, l):
    """
    :param k: numero de tabuas
    :param l: comprimento das tabuas
    :return: se é possivel cobrir a area do salão
    """
    area_tabuas = k * l
    return area_tabuas


def impossivel(k, largura, altura, l, comprimento):
    """
    :return: print dizendo que não foi possivel cobrir o salão
    """
    cont = 0
    tam = k * l
    if tam < largura:
        print("impossivel")
    else:
        for i in comprimento:
            if i < altura:
                cont += 1
    if cont == k:
        print("impossivel")
    pass


def calc():
    """
    :return: o calculo das tabuas para cobrir o salão
    """
    pass











