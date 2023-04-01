n, m = map(int, input().split())
tree = list(map(int, input().split()))

left, right = 1, max(tree)

while left <= right:
    mid = (left + right) // 2
    total = 0

    for t in tree:
        if t > mid:
            total += (t - mid)

    if total >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)