import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
mount = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
answer = 0

while True:
    cnt = 0
    red = [[-1]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mount[i][j] and red[i][j] == -1:
                cnt += 1
                if cnt >= 2:
                    print(answer)
                    sys.exit(0)
                queue = deque()
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    if red[x][y] != -1:
                        continue
                    red[x][y] = 0
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if mount[nx][ny] == 0:
                                red[x][y] += 1
                            elif red[nx][ny] == -1:
                                queue.append([nx, ny])
    if cnt == 0:  # 전부 0 일때
        break
    for i in range(n):  # 빙산 내려감
        for j in range(m):
            if red[i][j] != -1:
                mount[i][j] = max(0, mount[i][j]-red[i][j])
    answer += 1

print(0)
