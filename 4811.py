import sys
sys.stdin = open("input.txt", "r")

dp = [[-1 for _ in range(32)] for _ in range(61)]
dp[1][1] = 1
for i in range(2, 61):
    for j in range(31):
        if dp[i-1][j] >= 0:
            dp[i][j+1] = max(0, dp[i][j+1]) + dp[i-1][j]
            if j >= 1:
                dp[i][j-1] = max(0, dp[i][j-1]) + dp[i-1][j]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n*2][0])
