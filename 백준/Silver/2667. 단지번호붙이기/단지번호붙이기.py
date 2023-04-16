from collections import deque


def bfs(x, y):
    visit[x][y] = 1
    q = deque([(x, y)])
    house = [(x, y)]
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0 and board[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                    house.append((nx, ny))
    return house


n = int(input())

board = [[0] * n for _ in range(n)]
visit = [[0] * n for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(n):
        board[i][j] = int(line[j])

cnt = 0
houses = []
for x in range(n):
    for y in range(n):
        if visit[x][y] == 0 and board[x][y] == 1:
            cnt += 1
            house = bfs(x, y)
            houses.append(house)

print(cnt)
house_cnts = [len(house) for house in houses]
house_cnts.sort()
for cnt in house_cnts:
    print(cnt)
