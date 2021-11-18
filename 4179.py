import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = float('inf')
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
field = [list(input().strip()) for _ in range(n)]
fire = [[INF for _ in range(m)] for _ in range(n)]
me = [[INF for _ in range(m)] for _ in range(n)]
ans = INF


def bfs(a, b, temp):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and temp[x][y] + 1 < temp[nx][ny] and field[nx][ny] != '#':
                temp[nx][ny] = temp[x][y] + 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if field[i][j] == 'J':
            me[i][j] = 1
            field[i][j] = '.'
            bfs(i, j, me)
        if field[i][j] == 'F':
            fire[i][j] = 1
            field[i][j] = '.'
            bfs(i, j, fire)

for i in range(n):
    for j in range(m):
        if (i == 0 or j == 0 or i == n-1 or j == m-1) and field[i][j] != '#' and me[i][j] < fire[i][j]:
            ans = min(ans, me[i][j])

print(ans) if ans != INF else print('IMPOSSIBLE')
