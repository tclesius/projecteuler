def sieve_of_eratosthenes(n):
    n = [i for i in range(2, n)]

    for k in range(len(n)):
        for i in range(k + 1, len(n)):

            if n[i] != "Marked" and n[k] != "Marked":

                if n[i] % n[k] == 0:
                    n[i] = "Marked"

    return list(filter(lambda x: x != "Marked", n))


def sieve_of_sundaram(n):
    k = (n - 2) // 2
    integers_list = [True] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            integers_list[i + j + 2 * i * j] = False
            j += 1

    primes = []
    if n > 2:
        primes += [2]
    for i in range(1, k + 1):
        if integers_list[i]:
            primes += [2 * i + 1]
    return primes


print(sieve_of_sundaram(104744)[-1])
