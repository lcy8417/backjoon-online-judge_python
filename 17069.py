import sys
sys.stdin = open("input.txt", "r")

n = int(input())
dp = [[[0, 0, 0] for _ in range(n+1)] for _ in range(n+1)]
pipe = [[0 for _ in range(n+1)]] + [[0] +
                                    list(map(int, input().split())) for _ in range(n)]
dp[1][2][0] = 1
for i in range(1, n+1):
    for j in range(2, n+1):
        if not pipe[i][j]:
            dp[i][j][0] += dp[i][j-1][2] + dp[i][j-1][0]
            dp[i][j][1] += dp[i-1][j][2] + dp[i-1][j][1]
            if not pipe[i-1][j] and not pipe[i][j-1]:
                dp[i][j][2] += sum(dp[i-1][j-1])

print(sum(dp[n][n]))
