N=int(input())

for i in range(N):
    string=list(input().split())
    for j in string:
        print(j[::-1], end=' ')