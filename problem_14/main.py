def Collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + Collatz(n / 2)
    else:
        return 1 + Collatz((3 * n) + 1)


print(Collatz(837799))
