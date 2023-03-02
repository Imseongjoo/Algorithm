n,k = map(int, input().split())
a=[]
for i in range(1,round(n/2)+1):
    if n%i==0:
        a.append(i)
a.append(n)
try:
    print(a[k-1])
except:
    print(0)