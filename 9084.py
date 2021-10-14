import sys
sys.stdin = open("input.txt", "r")

T = int(input())

while T:
    T -= 1
    n = int(input())
    coin = [0] + list(map(int, input().split()))
    goal = int(input())
    dp = [0 for _ in range(goal+1)]
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(coin[i], goal+1):
            dp[j] += dp[j-coin[i]]

    print(dp[goal])
