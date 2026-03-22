a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

c = 0.0
d = 0.01
e = 100
f = len(a)


def g(h, i):
    return i * h


def j(k, l, m):
    return sum((g(h, m) - n) ** 2 for h, n in zip(k, l)) / f


def o(k, l, m):
    return sum(2 * (g(h, m) - n) * h for h, n in zip(k, l)) / f


for p in range(e):
    q = o(a, b, c)
    c -= d * q

    if p % 10 == 0:
        print(p, j(a, b, c), c)

print(c)

r = 7
print(g(r, c))