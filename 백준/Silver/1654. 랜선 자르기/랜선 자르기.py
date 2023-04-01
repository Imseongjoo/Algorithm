k, n = map(int, input().split())

lan = []

for i in range(k):
    lan.append(int(input()))

left, right = 1, max(lan)

while left < right:
    mid = (left + right+1) // 2

    cnt = 0
    for i in lan:
        cnt += (i//mid)

    if cnt >= n:
        left = mid
    else:
        right = mid -1

print(left)