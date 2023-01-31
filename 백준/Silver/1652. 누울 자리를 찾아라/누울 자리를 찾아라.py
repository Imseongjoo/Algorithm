n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))
width = 0
length = 0
for x in range(n):
    cnt1 = 0
    for y in range(n):
        if matrix[x][y] == '.': 
            cnt1 += 1
        else:
            if cnt1 >= 2:
                width += 1
            cnt1 = 0
    if cnt1 >= 2 : width += 1
for z in range(n):
    cnt2 = 0
    for w in range(n):
        if matrix[w][z] == '.': 
            cnt2 += 1
        else:
            if cnt2 >= 2:
                length += 1
            cnt2 = 0
    if cnt2 >= 2 : length += 1
print(width, length)