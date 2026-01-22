def transpose_matrix(a):
    b = [[0] * len(a) for _ in range(len(a[0]))]
    print(b)
    for i,j in enumerate(a):
        for x,y in enumerate(j):
            b[x][i]=y
            print("b[x][i] = ",b[x][i] ,x ,i)
    return b

print(transpose_matrix([[1,2,3],[4,5,6]]))