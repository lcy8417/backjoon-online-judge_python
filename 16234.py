import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, l, r = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
answer = 0

while True:
    ch = [[0] * n for _ in range(n)]
    empty = [[0] * n for _ in range(n)]
    queue = deque()
    pos = 1
    flag = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0:
                queue.append([i, j])
                total = city[i][j]
                cnt = 1
                ch[i][j] = pos
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < n and 0 <= ny < n and l <= abs(city[x][y] - city[nx][ny]) <= r and ch[nx][ny] == 0:
                            ch[nx][ny] = pos
                            queue.append([nx, ny])
                            total += city[nx][ny]
                            cnt += 1
                            flag = 1
                if cnt > 1:
                    for v in range(n):
                        for w in range(n):
                            if ch[v][w] == pos:
                                city[v][w] = total // cnt
                pos += 1
    if flag == 0:
        break
    answer += 1

print(answer)
