def subSet(arr):
    n = len(arr)
    a = []

    for i in range(2 ** n):
        x = []
        for j in range(i):
            if i & (1 << j):
                x.append(arr[j])
        a.append(x)

    return a


