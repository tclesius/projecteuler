def gauss(k):
    return (k ** 2 + k) // 2


def gaussWSQ(k):
    return k * (2 * k + 1) * (k + 1) // 6


print((gauss(100) ** 2) - gaussWSQ(100))
