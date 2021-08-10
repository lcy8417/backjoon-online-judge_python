import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
forest = [list(input()) for _ in range(n)]
mon_info = deque()
water_pos = deque()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(n):
    for j in range(m):
        if forest[i][j] == 'D':
            forest[i][j] = 2
        elif forest[i][j] == 'X':
            forest[i][j] = 1
        elif forest[i][j] == 'S':
            mon_info.append([i, j, 0])
            forest[i][j] = 1
        elif forest[i][j] == '*':
            water_pos.append([i, j])
            forest[i][j] = 1
        else:
            forest[i][j] = 0

while water_pos or mon_info:
    tmp1 = []
    tmp2 = []
    while water_pos:
        x, y = water_pos.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and forest[nx][ny] == 0:
                forest[nx][ny] = 1
                tmp1.append([nx, ny])

    while mon_info:
        x, y, cnt = mon_info.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and forest[nx][ny] != 1:
                if forest[nx][ny] == 2:
                    print(cnt+1)
                    sys.exit(0)
                else:
                    forest[nx][ny] = 1
                    tmp2.append([nx, ny, cnt+1])
    for x in tmp1:
        water_pos.append(x)
    for x in tmp2:
        mon_info.append(x)

print('KAKTUS')
