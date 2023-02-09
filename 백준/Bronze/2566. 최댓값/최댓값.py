a = [list(map(int, input().split())) for _ in range(9)]
tmp = 0
b = [0,0]
for y in range(0,9):
    for x in range(0,9):
        if a[y][x] > tmp:
            tmp = a[y][x]
            b = [y,x]
print(tmp)
print(b[0]+1,b[1]+1)