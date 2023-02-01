N, M = map(int, input().split())
ls = list(map(int, input().split()))
max_ls = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = ls[i]+ls[j]+ls[k]
            if ls[i]+ls[j]+ls[k] <= M:
                max_ls.append(sum)
print(max(max_ls))