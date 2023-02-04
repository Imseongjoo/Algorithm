import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
b = []
for i in range(N,M+1):
    a = []
    j = 1
    while i>=j:
        if i%j == 0:
            a.append(j)
            j += 1  
        elif i%j != 0:
            j += 1    
    if len(a) == 2:
        b.append(max(a))  
if len(b) != 0:
    print(sum(b))
    print(min(b))
else:
    print(-1)