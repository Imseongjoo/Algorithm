from collections import deque
import sys


def bfs(node):
    global cnt
    queue = deque()
    queue.append(node)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

    return 0


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[r] = 1
cnt = 1

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

bfs(r)
for i in visited[1:]:
    print(i)