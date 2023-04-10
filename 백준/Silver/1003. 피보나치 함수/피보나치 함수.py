T = int(input())
memo = [(1, 0), (0, 1)] + [None] * 39 
for i in range(2, 41):
    memo[i] = (memo[i-1][0]+memo[i-2][0], memo[i-1][1]+memo[i-2][1])
for _ in range(T):
    N = int(input())
    cnt_0, cnt_1 = memo[N]
    print(cnt_0, cnt_1)