
for _ in range(int(input())):   
    m, n = map(int, input().split())
    box = [[] for _ in range(n)]
    for i in range(m):
        a = list(input().split())
        for j in range(n):
            box[j].append(a[j])
    move = 0
    for i in range(n):
        num = box[i].count('1')
        floor = m-1

        for j in range(m-1, -1, -1):
            if box[i][j] == '1':
                move += floor-j
                floor -= 1
    print(move)