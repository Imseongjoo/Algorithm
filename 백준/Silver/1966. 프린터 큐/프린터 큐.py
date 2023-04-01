from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    priority = deque(range(n))

    cnt = 0
    while queue:
        if queue[0] == max(queue):
            queue.popleft()
            idx = priority.popleft()
            cnt += 1
            if idx == m:
                break
        else:
            queue.append(queue.popleft())
            priority.append(priority.popleft())

    print(cnt)