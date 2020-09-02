def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f())
    return fs


f1, f2, f3 = count()

print(f1)
print(f2)
print(f3)


def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs