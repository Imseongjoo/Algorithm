matrix = [list(map(int, input().split())) for i in range(4)]
a = []
for i in matrix:
    for j in range(i[0],i[2]):
        for k in range(i[1],i[3]):
            a.append((j,k))
print(len(set(a)))