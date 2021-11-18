from collections import deque
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

m, n = map(int, input().split())
field = [list(map(int, input().strip())) for _ in range(n)]
dis = [[10001 for _ in range(m)] for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
queue = deque()
queue.append((0, 0, 0))
dis[0][0] = field[0][0]
while queue:
    x, y, c = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if field[nx][ny] and dis[nx][ny] > c + 1:
                dis[nx][ny] = c+1
                queue.append((nx, ny, c+1))
            if not field[nx][ny] and dis[nx][ny] > c:
                dis[nx][ny] = c
                queue.append((nx, ny, c))

print(dis[n-1][m-1])
