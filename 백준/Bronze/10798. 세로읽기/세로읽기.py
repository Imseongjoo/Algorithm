a = [[0] * 15 for i in range(5)]
for i in range(5):
    ls = list(input())
    l = len(ls)
    for j in range(l):
        a[i][j] = ls[j]
for i in range(15):
    for j in range(5):
        if a[j][i] == 0:
            continue
        else:
            print(a[j][i], end='')