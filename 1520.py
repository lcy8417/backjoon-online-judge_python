import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]


def go(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] > graph[x][y]:
                dp[x][y] += go(nx, ny)
    return dp[x][y]


go(n-1, m-1)
print(dp[n-1][m-1])
