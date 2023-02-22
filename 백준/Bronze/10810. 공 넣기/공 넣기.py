N,M=map(int, input().split())
basket = [0]*N
for i in range(M):
    start, end, number = map(int, input().split())
    for j in range(start-1, end):
        basket[j] = number
for i in range(N):
    print(basket[i], end=' ')
print()   