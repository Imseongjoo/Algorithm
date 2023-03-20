from collections import deque

n = int(input())
a = deque([i for i in range(1, n+1)])

while 1:
    if len(a) == 1:
        print(a[0])
        break
    a.popleft()
    if len(a) == 1:
        print(a[0])
        break
    a.append(a.popleft())
    if len(a) == 1:
        print(a[0])
        break