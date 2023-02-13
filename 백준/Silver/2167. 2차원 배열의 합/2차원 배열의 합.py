N,M=map(int,input().split())
a = [list(map(int, input().split())) for _ in range(N)]
T=int(input())
for _ in range(T):
    i,j,x,y = map(int, input().split())
    res = 0
    for q in range(i-1,x):
        for w in range(j-1,y):
            res += a[q][w]
    print(res)