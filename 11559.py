import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

puyo = [list(input()) for _ in range(12)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ans = 0


def drop(x, y):
    for i in range(x-1, -1, -1):
        if puyo[i][y] != '.':
            puyo[i][y], puyo[x][y] = puyo[x][y], puyo[i][y]
            return


while True:
    q = deque()
    flag = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                ch = [[0 for _ in range(6)] for _ in range(12)]
                ch[i][j] = 1
                q.append([i, j])
                bomb = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < 12 and 0 <= ny < 6 and puyo[nx][ny] == puyo[i][j] and (nx, ny) not in bomb:
                            bomb.append((nx, ny))
                            q.append((nx, ny))
                if len(bomb) >= 4:
                    while bomb:
                        bx, by = bomb.pop()
                        puyo[bx][by] = '.'
                        flag = 1

    if not flag:
        break

    for i in range(11, -1, -1):
        for j in range(5, -1, -1):
            if puyo[i][j] == '.':
                drop(i, j)

    ans += 1

print(ans)
