n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

cnt = 0
i = coin[-1]
while k > 0:
    cnt += k//i
    k = k % i
    coin.pop(-1)
    if k < i and len(coin) > 0:
        i = coin[-1]

print(cnt)