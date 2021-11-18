import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque()
n = int(input())
field = [list(map(int, input().strip())) for _ in range(n)]
ch = [[[0 for _ in range(2*n)] for _ in range(n)] for _ in range(n)]
ans = n ** 3
q.append((0, 0, 0))
while q:
    x, y, z = q.popleft()
    if x == n-1 and y == n-1:
        ans = min(z, ans)
        continue
    if ch[x][y][z] or z >= ans:
        continue
    ch[x][y][z] = 1
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if field[nx][ny]:
                q.append((nx, ny, z))
            else:
                q.append((nx, ny, z+1))
print(ans)
