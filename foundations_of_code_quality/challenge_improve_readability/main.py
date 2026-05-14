def f(a):
    b = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            b += a[i]
        else:
            b -= a[i]
    return b

f([1, 2, 3, 4, 5])
