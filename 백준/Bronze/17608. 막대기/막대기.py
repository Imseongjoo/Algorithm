N=int(input())
a = []
for i in range(N):
    a.append(int(input()))
top = 0
cnt = 0    
for j in a[::-1]:
    if j>top:
        top = j
        cnt += 1
print(cnt)