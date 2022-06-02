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


n = 1
lst = []
while 1:
    f = fibonacci(n)
    if f > 4000000:
        break
    if f % 2 == 0:
        lst += [f]
    n += 1

print(sum(lst))
