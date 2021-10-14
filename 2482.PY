import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

mod = int(1e9+3)
n = int(input())
k = int(input())
dp = [[[0, 0, 0, 0] for _ in range(n+1)] for _ in range(k+1)]

for i in range(2, n+1):
    dp[1][i] = [i-2, 1, 1, 0]

for i in range(2, k+1):
    for j in range(i*2-1, n+1):
        dp[i][j][0] = (dp[i][j-1][1] + dp[i][j-1][0]) % mod
        dp[i][j][1] = dp[i-1][j-1][0] % mod
        dp[i][j][2] = (dp[i][j-1][2] + dp[i][j-1][3]) % mod
        dp[i][j][3] = dp[i-1][j-1][2] % mod

print(sum(dp[k][n][:3]) % mod)
