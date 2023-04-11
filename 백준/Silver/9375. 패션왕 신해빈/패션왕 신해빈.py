t = int(input())

for i in range(t):
    n = int(input())
    nude = {}
    for j in range(n):
        a, b = input().split()
        if b not in nude:
            nude[b] = 1
        else:
            nude[b] += 1

    count = 1
    for k in nude.values():
        count *= (k+1)
        
    count -= 1
    print(count)