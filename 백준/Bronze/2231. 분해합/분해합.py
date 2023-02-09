n = int(input())
b = []
for i in range(1,n+1):
    cnt = 0
    for j in str(i):
        cnt += int(j)
    a = cnt + i
    if a == n:
        b.append(i)
if len(b) == 0:
    print(0)
else:
    print(min(b))