from _functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num2(s):
    return DIGITS[s]


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num2, s))


print(str2int('12345'))

print(list(map(char2num2, "123")))
