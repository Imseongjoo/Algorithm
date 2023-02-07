N = int(input())
stu = []
for i in range(N):
    w, h = map(int, input().split())
    stu.append((w, h))

for cur in stu:
    rank = 1
    for next in stu:
        if (cur[0]!=next[0]) and (cur[1]!=next[1]):  
            if (cur[0]<next[0]) and (cur[1]<next[1]):
                rank += 1
    print(rank)