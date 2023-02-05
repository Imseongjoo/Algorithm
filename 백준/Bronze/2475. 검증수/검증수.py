ls=list(map(int,input().split()))
a = []
for i in ls:
    a.append(i*i)
print(sum(a)%10)