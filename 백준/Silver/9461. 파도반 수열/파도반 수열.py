import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]
dp = [1, 1, 1, 2, 2]

for i in range(5, max(arr)):
    dp.append(dp[i-1]+dp[i-5])

for i in arr:
    print(dp[i-1])