import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
dp = [[[0, 0] for _ in range(3)] for _ in range(3)]
for i in range(1, n+1):
    game = list(map(int, input().split()))
    dp[i % 3][0][0] = min(dp[i % 3-1][0][0], dp[i % 3-1][1][0]) + game[0]
    dp[i % 3][1][0] = min(dp[i % 3-1][0][0], dp[i % 3-1]
                          [1][0], dp[i % 3-1][2][0]) + game[1]
    dp[i % 3][2][0] = min(dp[i % 3-1][1][0], dp[i % 3-1][2][0]) + game[2]
    dp[i % 3][0][1] = max(dp[i % 3-1][0][1], dp[i % 3-1][1][1]) + game[0]
    dp[i % 3][1][1] = max(dp[i % 3-1][0][1], dp[i % 3-1]
                          [1][1], dp[i % 3-1][2][1]) + game[1]
    dp[i % 3][2][1] = max(dp[i % 3-1][1][1], dp[i % 3-1][2][1]) + game[2]

print(max(dp[n % 3][0][1], dp[n % 3][1][1], dp[n % 3][2][1]),
      min(dp[n % 3][0][0], dp[n % 3][1][0], dp[n % 3][2][0]))
