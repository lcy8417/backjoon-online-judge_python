import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def go(x, s, cnt):
    global minn
    if x >= n:
        return
    elif cnt == 3:
        queue = deque(birus)
        tmp = [list(graph[i]) for i in range(n)]
        tot = 0
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    tot += 1
                    if tot >= minn:
                        return
                    queue.append([nx, ny])
        minn = min(minn, tot)
        return
    else:
        for i in range(s, m):
            if graph[x][i] == 0:
                graph[x][i] = 1
                go(x, i+1, cnt+1)
                graph[x][i] = 0
        else:
            go(x+1, 0, cnt)


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
birus = []
graph = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]
answer = m * n
minn = 2147000000
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            birus.append([i, j])
            answer -= 1
        elif graph[i][j] == 1:
            answer -= 1


go(0, 0, 0)
print(answer - minn - 3)
