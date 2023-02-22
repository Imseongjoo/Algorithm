N,M=map(int, input().split())
basket =[]
for i in range(1,N+1):
    basket.append([i])
for j in range(M):
    a,b = map(int, input().split())
    basket[a-1],basket[b-1]=basket[b-1],basket[a-1]
for k in range(N):
    print(basket[k][0],end=' ')