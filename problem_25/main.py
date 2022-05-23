def rec_fibonacci(k):
    if k < 0:
        return
    if k <= 1:
        return k
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


def fibonacci(k):
    if k <= 2:
        return 1

    grandparent = 0
    parent = 1
    child = 0

    for i in range(2, k + 1):
        child = parent + grandparent
        grandparent = parent
        parent = child

    return child


n = 0
while 1:
    if len(list(repr(fibonacci(n)))) == 1000:
        break
    n += 1

print(n)
