def josephus(n, k):
    """
    :param n: The number of objects in the circle (array)
    :param k: The number of skips after an object is removed
    :return: The position of the final object left
    """
    if n == 1:
        return 1
    else:
        return (k - 1 + josephus(n - 1, k)) % n + 1


n = int(input())
k = int(input())
josephus(n, k)
print(josephus(n, k))


