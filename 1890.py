import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

dp[0][0] = 1
dp[n-1][n-1] = 0
for i in range(n):
    for j in range(n):
        if i == j == n-1:
            break
        if dp[i][j] != -1:
            x, y = i + game[i][j], j + game[i][j]
            if x < n:
                dp[x][j] = (max(0, dp[x][j]) + dp[i][j])
            if y < n:
                dp[i][y] = (max(0, dp[i][y]) + dp[i][j])

print(dp[n-1][n-1])
