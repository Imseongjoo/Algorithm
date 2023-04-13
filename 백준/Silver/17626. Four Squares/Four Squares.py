import sys, math
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    min_cnt = 4
    for j in range(int(math.sqrt(i)), 0, -1):
        min_cnt = min(min_cnt, dp[i-j**2]+1)
    dp.append(min_cnt)

print(dp[n])   