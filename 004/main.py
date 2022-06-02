def is_palindrome(n):
    ls = list(str(n))
    n = len(ls) // 2

    for i in range(n):
        if ls[0 + i] != ls[-1 - i]:
            return 0
    return 1


print(max([x * y for x in range(999) for y in range(999) if is_palindrome(x * y)]))
