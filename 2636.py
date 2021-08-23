import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


while True:
    ch = [[0]*m for _ in range(n)]
    cnt = 0
    queue = deque()
    ch[0][0] = 1
    queue.append([0, 0])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and ch[nx][ny] == 0:
                if square[nx][ny] != 1:
                    queue.append([nx, ny])
                ch[nx][ny] = 1

    for i in range(n):
        for j in range(m):
            if square[i][j] == 1:
                cnt += 1

    if cnt == 0:
        break

    answer[0] = cnt
    answer[1] += 1

    for i in range(n):
        for j in range(m):
            if square[i][j] and ch[i][j]:
                square[i][j] = 0
                cnt -= 1

print(answer[1])
print(answer[0])
