N = int(input())
K = list(map(int, input().split()))
ls = []
for i in K:
    ls.append(i)
S = set(ls)
print(N -len(S))