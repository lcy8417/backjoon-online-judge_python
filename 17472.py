import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

INF = 1000001
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF for _ in range(11)] for _ in range(11)]
f = [i for i in range(8)]
heap = []
cnt = 2
ans = INF


def find(x):
    if x == f[x]:
        return x
    f[x] = find(f[x])
    return f[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        f[y] = x
    else:
        f[x] = y


def bfs(a, b, c):
    q = deque()
    q.append((a, b))
    while q:
        a, b = q.popleft()
        if island[a][b] != 1:
            continue
        island[a][b] = c
        for k in range(4):
            nx, ny = a+dx[k], b+dy[k]
            if 0 <= nx < n and 0 <= ny < m and island[nx][ny] == 1:
                q.append((nx, ny))


def dfs(x, c, sum):
    global ans, f
    if sum > ans:
        return
    if len(c) == cnt - 3:
        f = [i for i in range(8)]
        temp = 0
        for dis, x, y in c:
            if find(x) == find(y):
                return
            union(x, y)
            temp += dis
        ans = min(temp, ans)
    else:
        for i in range(x, len(heap)):
            dfs(i+1, c + [heap[i]], sum + heap[i][0])


def connect(x, y, s, move):
    if move == 'right':
        for dis in range(1, m):
            if y+dis >= m:
                return
            next = island[x][y+dis]
            if next:
                if dis > 2:
                    dp[s][next] = min(dp[s][next], dis-1)
                return

    if move == 'down':
        for dis in range(1, n):
            if x+dis >= n:
                return
            next = island[x+dis][y]
            if next:
                if dis > 2:
                    dp[s][next] = min(dp[s][next], dis-1)
                return


for i in range(n):
    for j in range(m):
        if island[i][j] == 1:
            bfs(i, j, cnt)
            cnt += 1

for i in range(n):
    for j in range(m):
        if island[i][j]:
            if j+1 < m and not island[i][j+1]:
                connect(i, j, island[i][j], 'right')
            if i+1 < n and not island[i+1][j]:
                connect(i, j, island[i][j], 'down')

for i in range(2, 8):
    for j in range(2, 8):
        if dp[i][j] != INF:
            heap.append([dp[i][j], i, j])

heap.sort()

dfs(0, [], 0)
print(ans) if ans != INF else print(-1)
