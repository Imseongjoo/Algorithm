N = int(input())
ans = 0
for i in range(1,N+1):
    a = list(map(int,str(i)))
    if i < 100:
        ans += 1
    elif a[0]-a[1] == a[1]-a[2]:
        ans += 1
print(ans)