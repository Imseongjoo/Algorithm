matrix = [list(map(int, input().split())) for i in range(5)]
b = []
for j in matrix:
    a = sum(j)
    b.append(a)
    c = max(b)
print(b.index(c)+1, c)