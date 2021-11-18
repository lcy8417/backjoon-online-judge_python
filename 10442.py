import sys
sys.stdin = open("input.txt", "r")

T = int(input())

mod = 1_000_000_007
dp = [[0 for _ in range(5002)] for _ in range(5002)]
dp[1][1] = 1
for i in range(1, 5000):
    for j in range(5001):
        if j == 0:
            dp[i+1][j+1] += dp[i][j] % mod
        elif j == 5000:
            dp[i+1][j-1] += dp[i][j] % mod
        else:
            dp[i+1][j+1] += dp[i][j] % mod
            dp[i+1][j-1] += dp[i][j] % mod

while T:
    T -= 1
    n = int(input())
    print(dp[n][0] % mod)
