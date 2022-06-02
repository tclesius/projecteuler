import math

a = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
     'ten', 'eleven', 'twelve', 'thirteen', 'fourteen']
b = ['teen', 'ty']
c = ['', '', 'twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine']
d = ['hundred', 'thousand']


def tens_ones(n, with_zero=True):
    l = list(str(n))
    ones_digit = int(l[-1])
    if n >= 10:
        tens_digit = int(l[-2])

    if n >= 20:
        return c[tens_digit] + b[1] + a[ones_digit]

    if n >= 15:
        return c[ones_digit] + b[0]

    if n >= 1:
        return a[n]

    if n == 0 and with_zero:
        return "zero"
    else:
        return ""


def hundreds(n):
    l = list(str(n))
    hundreds_digit = int(l[-3])

    return a[hundreds_digit] + " " + d[0]


def converter(n):
    l = list(str(n))

    if n == 1000:
        return "one thousand"
    if n >= 100:
        tens_ones_digits = int("".join(list([l[-2], l[-1]])))
        if tens_ones_digits != 0:
            return hundreds(n) + " and " + tens_ones(tens_ones_digits)
        else:
            return hundreds(n)
    if n <= 99:
        return tens_ones(n)


x = [len(converter(i).replace(' ', '')) for i in range(1, 1001)]

print(sum(x))
