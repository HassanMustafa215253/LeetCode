def matrix_dot_vector(a, b) :
    c = [0] * len(b)
    if len(a[0]) != len(b):
        return -1
    print(a)
    print(b)
    for j, i in enumerate(a):
        print("i = ", i)
        for x, y in enumerate(b):
            c[j] += i[x] * y
        print("x = ", x)
        print("y = ", y)
    return c

print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))
