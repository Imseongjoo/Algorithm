N = int(input())
ls = list(map(int, input().split()))
cnt = 0
for i in ls:
    a = []
    j = 1
    while i>=j:
        if i%j == 0:
            a.append(i)
            j += 1
        else:
            j += 1
    if len(a) == 2:
        cnt += 1
print(cnt)