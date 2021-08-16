import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0


def go(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n and field[x][y] > field[nx][ny]:
            dp[x][y] = max(dp[x][y], go(nx, ny)+1)

    return dp[x][y]


for i in range(n):
    for j in range(n):
        ans = max(ans, go(i, j))

print(ans)
