import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

k = int(input())
m, n = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
dis = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
answer = 2147000000
queue = deque()
hx, hy = [2, 1, -1, -2, -2, -1, 1, 2], [-1, -2, -2, -1, 1, 2, 2, 1]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if field[i][j]:
            dis[i][j][0] = 1

field[0][0] = 1
queue.append([0, 0, 0])
while queue:
    x, y, z = queue.popleft()
    if x == n-1 and y == m-1:
        answer = dis[x][y][z]
        break
    for v in range(4):
        nx, ny = x+dx[v], y+dy[v]
        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0 and dis[nx][ny][z] == 0:
            dis[nx][ny][z] = dis[x][y][z] + 1
            queue.append([nx, ny, z])
    if z < k:
        for v in range(8):
            nx, ny = x+hx[v], y+hy[v]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0 and dis[nx][ny][z+1] == 0:
                dis[nx][ny][z+1] = dis[x][y][z] + 1
                queue.append([nx, ny, z+1])

# for i in range(n):
#     for j in range(m):
#         print(field[i][j], end=' ')
#     print()


if answer == 2147000000:
    print(-1)
else:
    print(answer)
