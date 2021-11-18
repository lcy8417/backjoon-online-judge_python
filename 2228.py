import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = -2147000000
n, m = map(int, input().split())

dp = [[0 if i == 0 else INF for _ in range(n+2)] for i in range(m+1)]
cSum = [[0 for _ in range(n+2)] for _ in range(n+2)]
a = [0, 0]

for i in range(n):
    a.append(int(input()))

for i in range(2, n+2):
    for j in range(2, n+2):
        cSum[i][j] = sum(a[i:j+1])

for i in range(1, m+1):
    for j in range(i*2, n+2):
        for k in range(i*2-2, j-1):
            dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][k] + cSum[k+2][j])

print(dp[m][n+1])
