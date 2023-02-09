ls = []
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    for y in range(b,b+10):
        for x in range(a,a+10):
            ls.append((x,y))
print(len(set(ls)))