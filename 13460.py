import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
queue = deque()
goal, blue, red = [0, 0], [0, 0], [0, 0]
machine = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'O':
            goal[0], goal[1] = i, j
            continue
        elif lst[i][j] == 'R':
            red[0], red[1] = i, j
        elif lst[i][j] == 'B':
            blue[0], blue[1] = i, j
        elif lst[i][j] == '#':
            machine[i][j] = 1

queue.append([red[0], red[1], blue[0], blue[1], 0])
while queue:
    rx, ry, bx, by, cnt = queue.popleft()
    if cnt >= 10:
        break
    for k in range(4):
        nrx, nry, nbx, nby = rx, ry, bx, by
        while True:
            if goal == [nbx, nby]:
                break
            if goal == [nrx, nry]:
                flag = 0
                while True:
                    if machine[nbx][nby]:
                        break
                    if [nbx, nby] == goal:
                        flag = 1
                        break
                    nbx, nby = nbx+dx[k], nby+dy[k]
                if not flag and cnt < 10:
                    print(cnt+1)
                    sys.exit(0)
                else:
                    queue.append([rx, ry, bx, by, cnt+1])
                    break
            if machine[nrx+dx[k]][nry+dy[k]] and machine[nbx+dx[k]][nby+dy[k]]:  # 둘다 벽에 막혔으면 그전의 값 대입
                if ([nrx, nry] != [rx, ry]) or ([nbx, nby] != [bx, by]):
                    queue.append([nrx, nry, nbx, nby, cnt+1])
                break
            if (machine[nrx+dx[k]][nry+dy[k]] and [nbx+dx[k], nby+dy[k]] == [nrx, nry]) or\
                    (machine[nbx+dx[k]][nby+dy[k]] and [nrx+dx[k], nry+dy[k]] == [nbx, nby]):
                if ([nrx, nry] != [rx, ry]) or ([nbx, nby] != [bx, by]):
                    queue.append([nrx, nry, nbx, nby, cnt+1])
                break
            if machine[nrx+dx[k]][nry+dy[k]] == 0:
                nrx, nry = nrx+dx[k], nry+dy[k]
            if machine[nbx+dx[k]][nby+dy[k]] == 0:
                nbx, nby = nbx+dx[k], nby+dy[k]

print(-1)
