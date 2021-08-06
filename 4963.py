import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

dx, dy = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, -1, 1, -1, 1]

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    island = [list(map(int, input().split())) for _ in range(m)]
    queue = deque()
    answer = 0
    for i in range(m):
        for j in range(n):
            if island[i][j]:
                queue.append([i, j])
                island[i][j] = 0
                answer += 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and island[nx][ny]:
                            island[nx][ny] = 0
                            queue.append([nx, ny])
    print(answer)
