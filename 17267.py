import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m = map(int, input().split())
l, r = map(int, input().split())
field = [list(map(int, input())) for _ in range(n)]
ch = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
answer = 0

for i in range(n):
    for j in range(m):
        if field[i][j] == 2:
            field[i][j] = 0
            queue.append([i, j, 0, 0])
            ch[i][j] = 1
            answer += 1

while queue:
    x, y, lcnt, rcnt = queue.popleft()
    tx = x-1
    while tx >= 0 and field[tx][y] == 0 and ch[tx][y] == 0:
        ch[tx][y] = 1
        answer += 1
        queue.append([tx, y, lcnt, rcnt])
        tx -= 1
    tx = x+1
    while tx < n and field[tx][y] == 0 and ch[tx][y] == 0:
        ch[tx][y] = 1
        answer += 1
        queue.append([tx, y, lcnt, rcnt])
        tx += 1
    if lcnt < l and 0 <= y-1 and field[x][y-1] == 0 and ch[x][y-1] == 0:
        ch[x][y-1] = 1
        answer += 1
        queue.append([x, y-1, lcnt+1, rcnt])
    if rcnt < r and y+1 < m and field[x][y+1] == 0 and ch[x][y+1] == 0:
        ch[x][y+1] = 1
        answer += 1
        queue.append([x, y+1, lcnt, rcnt+1])


print(answer)
