N = int(input())
a = []
for i in range(1,N+1):
    a.append(int(input()))
b = sorted(a)
for i in range(len(b)):
    print(b[i])