def devisors_count(n):
    result = 0
    sqrt_n = int(n ** 0.5)

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            result += 1

    result *= 2

    if sqrt_n ** 2 == n:
        result -= 1

    return result


def gauss(k):
    return (k ** 2 + k) // 2


def triangle_number(divisors):
    n = 1
    while 1:
        tri_num = gauss(n)
        if devisors_count(tri_num) > divisors:
            return tri_num
        n += 1


print(triangle_number(500))
