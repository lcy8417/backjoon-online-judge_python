import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 2147000000
n, m = map(int, input().split())
imp = [0 for _ in range(n+1)]
for x in list(map(int, input().split())):
    imp[x] = 1
dp = [[INF for _ in range(106)] for _ in range(106)]
dp[0][0] = 0
for i in range(n+1):  # 날짜 반복문
    for j in range(41):  # 쿠폰 반복문
        if dp[i][j] == INF:
            continue
        if i+1 <= n and imp[i+1]:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        dp[i+1][j] = min(dp[i+1][j], dp[i][j]+10000)
        for k in range(1, 4):
            dp[i+k][j+1] = min(dp[i+k][j+1], 25000 + dp[i][j])
        for k in range(1, 6):
            dp[i+k][j+2] = min(dp[i+k][j+2], 37000 + dp[i][j])
        if j >= 3:
            dp[i+1][j-3] = min(dp[i][j], dp[i+1][j-3])

print(min(dp[n]))
