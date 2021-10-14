import sys
sys.stdin = open("input.txt", "r")

n = int(input())
chd = []
dp = [0 for _ in range(n)]
for i in range(n):
    chd.append(int(input()))
    for j in range(i):
        if chd[j] < chd[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(n-max(dp))
