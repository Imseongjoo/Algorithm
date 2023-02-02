N = int(input())
P = list(map(int, input().split()))
S = []
sum = 0
for i in range(1,N):
    if P[i-1]<P[i]:
        sum += P[i]-P[i-1]
        if i == N-1:
            S.append(sum)
    else:
        S.append(sum)
        sum = 0
print(max(S))