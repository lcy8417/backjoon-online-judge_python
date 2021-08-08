import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(input())
color = [list(input()) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
queue = deque()
normal, abnormal = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def swp(x):
    if x == 'R':
        return 'G'
    else:
        return x


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    ch[a][b] = 1
    cur = color[a][b]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and color[nx][ny] == cur and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                queue.append([nx, ny])


for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            normal += 1
            bfs(i, j)

color = [list(map(swp, color[i])) for i in range(n)]
ch = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            abnormal += 1
            bfs(i, j)

print(normal, abnormal)
