def evenly_divideable(n, start, end):
    for x in range(start, end):
        if n % x != 0:
            return 0
    return 1


n = 1
while not evenly_divideable(n, 1, 20):
    n += 1

print(n)
