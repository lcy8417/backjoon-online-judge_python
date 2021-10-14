import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = max(1, sum(dp[i-1]))
        for j in range(1, 10):
            dp[i][j] = max(1, dp[i][j-1] - dp[i-1][j-1])
    print(sum(dp[n]))
