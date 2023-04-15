from collections import deque

def bfs(x, y):
    visit[x][y] = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == 0 and matrix[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append((nx, ny))

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    cnt = 0
    for x in range(n):
        for y in range(m):
            if visit[x][y] == 0 and matrix[x][y] == 1:
                bfs(x, y)
                cnt += 1
    
    print(cnt)
