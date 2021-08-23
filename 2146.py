import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]
ch = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
answer = 2147000000
queue = deque()
index = 0
for i in range(n):
    for j in range(n):
        if island[i][j] and ch[i][j] == 0:
            index += 1
            ch[i][j] = 1
            island[i][j] = index
            queue.append([i, j])
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n and island[nx][ny] and ch[nx][ny] == 0:
                        ch[nx][ny] = 1
                        island[nx][ny] = index
                        queue.append([nx, ny])

for i in range(n):
    for j in range(n):
        if island[i][j]:
            ch = [[0 for _ in range(n)] for _ in range(n)]
            queue.clear()
            queue.append([i, j, 0])
            cur = island[i][j]
            while queue:
                x, y, cnt = queue.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0:
                        if island[nx][ny] == 0:
                            ch[nx][ny] = 1
                            queue.append([nx, ny, cnt+1])
                        elif island[nx][ny] and island[nx][ny] != cur:
                            answer = min(answer, cnt)
                            queue.clear()
                            break

print(answer)
