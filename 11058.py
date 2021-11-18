import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n-2):
    for j in range(i+3, n+1):
        dp[j] = max(dp[j], dp[i]*(j-i-1))

print(dp[n])
