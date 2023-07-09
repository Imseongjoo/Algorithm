n = int(input())
len = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = 0
min_cost = cost[0]

for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    res += min_cost * len[i]
    
print(res)