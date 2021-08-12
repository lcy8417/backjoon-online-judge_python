import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
n, m = map(int, input().split())
island = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if island[i][j] == 'L':
            ch = [[0]*m for _ in range(n)]
            queue = deque()
            ch[i][j] = 1
            queue.append([i, j, 0])
            while queue:
                x, y, cnt = queue.popleft()
                answer = max(answer, cnt)
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and island[nx][ny] == 'L' and ch[nx][ny] == 0:
                        ch[nx][ny] = 1
                        queue.append([nx, ny, cnt+1])
print(answer)
