n,m = map(int, input().split())
a = []
for _ in range(0,n+1):
    a.append(_)
for _ in range(m):
    i,j,k = map(int,input().split())
    a = a[:i]+a[k:j+1]+a[i:k]+a[j+1:]
a.remove(0)
print(*a)