import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(r):
    global cnt
    visited[r] = cnt
    graph[r].sort()
    for i in graph[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


dfs(r)

for i in range(1, n + 1):
    print(visited[i])