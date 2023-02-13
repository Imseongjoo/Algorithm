N,M = map(int, input().split())
d = []
b = []
for i in range(N):
    d.append(input())
for i in range(M):
    b.append(input())
a = set(d)
c = set(b)
print(len(a.intersection(c)))
print(*sorted(a.intersection(c)),sep='\n')