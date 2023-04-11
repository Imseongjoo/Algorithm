n=int(input())
stair = []
for i in range(n):
    stair.append(int(input()))
    
dp=[0]*(n)

if len(stair) <= 2:
    print(sum(stair))
    
else:
    dp[0]=stair[0]
    dp[1]=stair[0]+stair[1]
    for j in range(2,n):
        dp[j]=max(dp[j-3]+stair[j-1]+stair[j], dp[j-2]+stair[j])
    print(dp[-1])

