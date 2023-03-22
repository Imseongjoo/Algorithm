n, m = map(int, input().split())
board = []
cnt = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'B':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[k][l] != 'B':
                        black += 1
                    else:
                        white += 1
        cnt.append(black)
        cnt.append(white)
print(min(cnt))
