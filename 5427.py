import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
INF = 1000001
T = int(input())
while T:
    T -= 1
    ans = INF
    me = deque()
    fire = deque()
    n, m = map(int, input().split())
    bding = [list(input().strip()) for _ in range(m)]
    dis1 = [[INF for _ in range(n)] for _ in range(m)]
    dis2 = [[INF for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if bding[i][j] == '*':
                fire.append((i, j, 1))
                dis1[i][j] = 1
            if bding[i][j] == '@':
                me.append((i, j, 1))
                bding[i][j] = '.'
                dis2[i][j] = 1

    while fire:
        x, y, t = fire.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and bding[nx][ny] == '.' and dis1[nx][ny] == INF:
                dis1[nx][ny] = t+1
                fire.append((nx, ny, t+1))

    while me:
        x, y, t = me.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and bding[nx][ny] == '.' and dis2[nx][ny] == INF:
                dis2[nx][ny] = t+1
                me.append((nx, ny, t+1))

    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0 or i == m-1 or j == n-1) and dis2[i][j] < dis1[i][j]:
                ans = min(dis2[i][j], ans)
    print(ans if ans != INF else 'IMPOSSIBLE')
